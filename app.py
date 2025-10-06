import cv2
import streamlit as st
import pandas as pd
import numpy as np
import io

from paddleocr import PPStructure


st.set_page_config(
    page_title="Data Tables Extractor",
    page_icon="📄",
    layout="wide"
)

with st.sidebar:
    st.header("1. Upload Your Image")
    uploaded_file = st.file_uploader(
        "Choose an image file", 
        type=['png', 'jpg', 'jpeg'],
        label_visibility="collapsed"
    )
    
    st.markdown("<h3 style='text-align: center; color: grey;'>OR</h3>", unsafe_allow_html=True)


    if st.button("Use Sample Image", use_container_width=True):
        with open("./sample/QlC7W.png", "rb") as f:
            sample_image_bytes = f.read()
        st.session_state['image_bytes'] = sample_image_bytes
        st.session_state['file_name'] = "QlC7W.png"
    
    st.markdown("---")
    st.header("2. About This App")
    st.info(
        "Manual data entry from tables is a major source of operational cost and errors for finance, logistics, "
        "and research teams. This demo showcases a powerful AI solution that can automate this process, " \
        "saving dozens of hours per week and ensuring data accuracy."
    )

st.title("📄 AI-Powered Document Table Extractor")
st.markdown("Instantly convert tables from scanned documents, invoices, or reports into clean, usable spreadsheet data.")


@st.cache_resource
def load_ocr_engine():
    return PPStructure(
        table_model_dir="inference/en_ppstructure_mobile_v2.0_SLANet_infer",
        table_char_dict_path="inference/table_structure_dict.txt",
        show_log=False
    )
ocr_engine = load_ocr_engine()


@st.cache_data
def process_image(image_bytes):
    """Takes image bytes, runs OCR, and returns a list of DataFrames."""
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    outputs = ocr_engine(img)
    
    dataframes = []
    html_outputs = []
    
    for region in outputs:
        if region['type'].lower() == 'table' and len(region['res']) > 0 and 'html' in region['res']:
            html_code = region['res']['html']
            try:
                dfs_from_html = pd.read_html(io.StringIO(html_code))
                if dfs_from_html:
                    dataframes.extend(dfs_from_html)
                    html_outputs.append(html_code)
            except Exception as e:
                st.warning(f"Could not parse a table from HTML. Error: {e}")
                
    return dataframes, html_outputs


image_to_process = None
if uploaded_file is not None:
    image_to_process = uploaded_file.getvalue()
    # Clear any sample image from state if a new file is uploaded
    st.session_state.pop('image_bytes', None) 
elif 'image_bytes' in st.session_state:
    image_to_process = st.session_state['image_bytes']

if image_to_process:
    st.image(image_to_process, caption="Image being processed", width=400)
    
    with st.spinner("🤖 AI is analyzing the table... Please wait."):
        extracted_dataframes, raw_html_list = process_image(image_to_process)

    if extracted_dataframes:
        st.success(f"✅ Found and extracted {len(extracted_dataframes)} table(s)!")
        
        for i, df in enumerate(extracted_dataframes):
            st.subheader(f"Extracted Table {i+1}")
            st.dataframe(df)
            
            st.download_button(
                label=f"📥 Download Table {i+1} as CSV",
                data=df.to_csv(index=False).encode('utf-8'),
                file_name=f'extracted_table_{i+1}.csv',
                mime='text/csv',
                key=f'download_button_{i}'
            )
            
            with st.expander(f"Show Raw HTML for Table {i+1}"):
                st.code(raw_html_list[i], language="html")

    else:
        st.warning("Could not find any tables in the uploaded image. Please try another one.")
else:
    st.info("👈 Upload an image or use the sample in the sidebar to get started!")