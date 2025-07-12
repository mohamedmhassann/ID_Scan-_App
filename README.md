# 🪪 ID Card OCR Scanner

A powerful web application built with Streamlit to extract text from ID card images using Tesseract OCR. This tool is designed to be simple, efficient, and user-friendly.

![App Screenshot](https://user-images.githubusercontent.com/10359910/188335001-25f3f27e-2c0a-4417-a72a-2f5e2cf5f6f1.png)
*(Replace this with a screenshot of your running application)*

---

## ✨ Features

-   **Easy Image Upload:** Supports `JPG`, `JPEG`, and `PNG` image formats.
-   **Advanced OCR:** Utilizes the Tesseract OCR engine for high-accuracy text extraction.
-   **Image Pre-processing:** Automatically handles different image channel formats (RGB, RGBA, Grayscale) and converts them for optimal OCR performance using OpenCV.
-   **Clean Output:** Displays extracted text in a clean, line-by-line format for easy reading.
-   **Raw Text View:** Provides an expandable section to view the full, raw extracted text.
-   **User-Friendly Interface:** A clean, professional, and responsive UI built with Streamlit.
-   **Cross-Platform:** Includes a check to automatically configure the Tesseract path for Windows users, ensuring it works out-of-the-box.

## 🛠️ Technologies Used

-   **Python:** The core programming language.
-   **Streamlit:** For building the interactive web application.
-   **OpenCV:** For image processing and manipulation.
-   **Pytesseract:** A Python wrapper for Google's Tesseract-OCR Engine.
-   **Pillow (PIL):** For handling image files.
-   **Numpy:** For numerical operations on image arrays.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

1.  **Python 3.8+:** Make sure you have Python installed. You can download it from python.org.

2.  **Tesseract OCR Engine:** This is a mandatory dependency that `pytesseract` wraps.
    -   **Windows:** Download and install it from Tesseract at UB Mannheim. The script is pre-configured for the default installation path (`C:\Program Files\Tesseract-OCR\tesseract.exe`). If you install it elsewhere, please update the path in `app.py`.
    -   **macOS (using Homebrew):**
        ```bash
        brew install tesseract
        ```
    -   **Linux (Debian/Ubuntu):**
        ```bash
        sudo apt-get update
        sudo apt-get install tesseract-ocr
        ```

### Installation

1.  **Clone the repository (or use your local project folder):**
    ```bash
    git clone https://github.com/your-username/id-scan-app.git
    cd id-scan-app
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  Execute the following command in your terminal from the project root directory:
    ```bash
    streamlit run app.py
    ```
2.  Your web browser should automatically open with the application running. If not, navigate to the local URL provided in the terminal (usually `http://localhost:8501`).

## Usage

1.  Launch the application as described above.
2.  Click on **"📤 Upload your ID Image"** to select an image file from your computer.
3.  The app will display the uploaded image and a spinner while it processes the text.
4.  Once complete, the extracted text will be displayed line by line.
5.  To see the complete, unprocessed output, expand the **"🔎 Show Full Extracted Text"** section.

## ✍️ Author

-   **Mohamed Mostafa**

Built with ❤️ using Python & Streamlit.