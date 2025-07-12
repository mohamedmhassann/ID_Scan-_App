import streamlit as st 
import cv2
import pytesseract
import numpy as np
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="🪪 ID Card OCR App", layout="centered")

# رأس الصفحة بتنسيق احترافي
st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #f0f4f8; border-radius: 10px;'>
        <h1 style='color: #112D4E;'>🪪 ID Card OCR Scanner</h1>
        <p style='color: #3F72AF; font-size: 18px;'>Extract text from ID cards using advanced OCR technology.</p>
    </div>
    <hr style='margin-top: 20px; border: 1px solid #ddd;' />
""", unsafe_allow_html=True)

# رفع الصورة
upload_img = st.file_uploader("📤 Upload your ID Image", type=["jpg", "jpeg", "png"])

# تهيئة Tesseract (مسار Windows فقط)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# دالة استخراج النص
def extract_text_from_image(image):
    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    elif image.shape[2] == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray)

# عند رفع صورة
if upload_img is not None:
    img = Image.open(upload_img)
    img_array = np.array(img)

    st.image(img_array, caption="🖼️ Uploaded ID", use_column_width=True)

    with st.spinner("🔍 Extracting text..."):
        ext_text = extract_text_from_image(img_array)
        text_list = [line.strip() for line in ext_text.splitlines() if line.strip()]

    st.success("✅ Text extracted successfully!")

    st.markdown("### 📄 Extracted Lines:")
    if text_list:
        for idx, line in enumerate(text_list, start=1):
            st.markdown(f"- **Line {idx}:** {line}")
    else:
        st.warning("⚠️ No text was extracted. Please try a clearer image.")

    with st.expander("🔎 Show Full Extracted Text"):
        st.code(ext_text, language='text')

# قسم About داخل Expander
with st.expander("ℹ️ About This App"):
    st.markdown("""
        ### 💡 Idea:
        This application is designed to automatically extract text from ID card images using **OCR (Optical Character Recognition)** technology. It’s especially useful for quickly reading information from scanned documents, IDs, or printed text.

        ### ⚙️ How It Works:
        - The app uses **Tesseract OCR** to process uploaded images.
        - Images are preprocessed for better recognition (grayscale, cleanup).
        - The text is displayed line-by-line dynamically.

        ### 👨‍💻 Developed By:
        **Mohamed Mostafa**
        
        Built with ❤️ using Python and Streamlit.
    """)

# فاصل سفلي
st.markdown("<hr style='border-top: 1px solid #ccc; margin-top:40px;' />", unsafe_allow_html=True)
