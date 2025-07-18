# 📄 Data Tables Extractor with OCR

This is a web application built with Streamlit that uses the power of PaddleOCR to extract tabular data directly from images. It's a demonstration of how AI can be used to solve common, tedious data entry problems.



## 🚀 Live Demo

You can try the live application here:
**[here](https://here)**

---

## The Problem

Manually transcribing data from tables locked in images (scans, photos, screenshots) is slow, frustrating, and prone to human error. This is a low-value task that consumes hours of valuable time for researchers, analysts, and administrators.

This project is an example of my philosophy as a **"Practical AI Builder"**: using powerful AI tools to create simple, useful solutions for real-world problems.

## ✨ Features

*   **Interactive File Uploader:** Easily upload your own `png`, `jpg`, or `jpeg` files.
*   **Sample Image:** Instantly test the app's functionality with a built-in sample image.
*   **AI-Powered OCR:** Leverages the robust PPStructure model from PaddleOCR to recognize and parse table structures.
*   **Interactive Data Display:** View the extracted table in a clean, interactive `pandas` DataFrame.
*   **CSV Download:** Download the extracted data as a clean `.csv` file with a single click.
*   **Behind the Scenes:** View the raw HTML output from the OCR engine to see how the data was structured.

## 🛠️ Tech Stack

*   **Framework:** Streamlit
*   **OCR Engine:** PaddleOCR (PPStructure)
*   **Data Handling:** Pandas, OpenCV, NumPy
*   **Language:** Python

---

## ⚙️ Setup and Installation

To run this application locally, please follow these steps:

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2. Create and activate a virtual environment:**
```bash
# For Mac/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

## ▶️ How to Run the App

```bash
streamlit run app.py
```

--- 

## 🧠 Key Learnings & Challenges

Building this project provided several key insights:

- **Performance is Key:** The OCR model is heavy and slow to load. Implementing Streamlit's caching (`@st.cache_resource` for the model and `@st.cache_data` for the processing function) was crucial for creating a responsive user experience.
- **Robust Code over Shortcuts:** The initial version of the code wrote a temporary Excel file to disk. I refactored this to process the OCR's HTML output directly in memory using `pandas.read_html` and `io.StringIO`. This is a cleaner, faster, and more portable approach that avoids filesystem issues, especially in deployed environments.
- **User Experience (UX) Matters:** Moving from a simple script to an interactive app involved thinking critically about the user's journey. Adding a sample image, spinners during processing, and clear download buttons transformed the project from a technical demo into a genuinely useful tool.

## 🔮 Future Improvements

- Support for multi-page PDFs.
- Allowing the user to draw a bounding box to select a specific table on a busy page.
- Integration with other OCR engines (like Tesseract) for comparison.
- Deploying the application using a more robust service like Docker on a cloud provider for higher traffic.

---

## Let's Connect

I'm always open to starting new conversations. Whether you have a question, a project idea, or just want to talk about technology and its impact, please don't hesitate to get in touch.

*   **Reach out via my email: marolahyrabe@gmail.com**
*   **Connect with me on [LinkedIn](https://www.linkedin.com/in/andriamarolahy-rabetokotany/)**