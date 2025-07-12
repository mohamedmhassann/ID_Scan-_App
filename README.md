# 🪪 ID Card OCR Scanner

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red.svg)](https://streamlit.io)
[![Tesseract](https://img.shields.io/badge/Tesseract-5.0%2B-brightgreen.svg)](https://github.com/tesseract-ocr/tesseract)

A user-friendly web application built with Python and Streamlit to extract text from ID card images using advanced Optical Character Recognition (OCR) technology.

![App Screenshot](https://user-images.githubusercontent.com/your-username/your-repo/assets/screenshot.png) 
*Replace the link above with a screenshot of your running application.*

---

## 💡 Overview

This application provides a simple interface to upload an image of an ID card (or any document with text) and instantly extracts the text content. It leverages the powerful Tesseract OCR engine and presents the results in a clean, readable format.

## ✨ Features

- **Easy Image Upload**: Supports `jpg`, `jpeg`, and `png` image formats.
- **Powerful OCR Engine**: Uses Tesseract for high-accuracy text recognition.
- **Image Preprocessing**: Automatically converts images to grayscale for better OCR results.
- **Clean & Organized Output**: Displays extracted text line-by-line.
- **Raw Text View**: Includes an expandable section to see the full, unprocessed text output.
- **User-Friendly Interface**: Built with Streamlit for a seamless user experience.

## ⚙️ Technology Stack

- **Backend**: Python
- **Web Framework**: Streamlit
- **OCR Engine**: Tesseract
- **Image Processing**: OpenCV, Pillow, NumPy

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### 1. Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8 or higher**
- **Tesseract OCR Engine**
  - **Windows**: Download and run the installer from Tesseract at UB Mannheim. **Important:** During installation, make sure to add Tesseract to your system's `PATH` variable.
  - **macOS**: `brew install tesseract`
  - **Linux (Debian/Ubuntu)**: `sudo apt-get install tesseract-ocr`

### 2. Installation & Setup

**A. Clone the repository:**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**B. Create and activate a virtual environment (recommended):**
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**C. Install the required Python packages:**
```bash
pip install -r requirements.txt
```

**D. Configure the Tesseract Path (if needed):**

The application will try to use Tesseract from your system's PATH. However, if you installed Tesseract in a custom location (especially on Windows) and it's not in your PATH, you may need to specify the path to the executable directly in `app.py`.

Open `app.py` and modify the following line with your Tesseract installation path:
```python
# In app.py
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 3. How to Run

Once the setup is complete, run the Streamlit application with the following command:

```bash
streamlit run app.py
```

Your web browser should automatically open to the application's URL (usually `http://localhost:8501`).

---

## 📂 Project Structure

```
ID_Scan_App/
├── app.py              # Main Streamlit application script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## 👨‍💻 Author

- **Mohamed Mostafa**