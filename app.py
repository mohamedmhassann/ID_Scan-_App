import streamlit as st 
import cv2
import pytesseract
import numpy as np
from PIL import Image
import platform  # 🆕 لمعرفة نظام التشغيل

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

# التحقق من نظام التشغيل وضبط المسار إن لزم
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# في لينكس (Streamlit Cloud)، لا حاجة لتغيير المسار

# رفع الصورة
upload_img = st.file_uploader("📤 Upload your ID Image", type=["jpg", "jpeg", "png"])

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

# قسم About دائم
st.markdown("""
    <hr style='margin-top:40px; border-top: 1px solid #bbb;' />
    <div style='background-color: #f9f9f9; padding: 25px; border-radius: 10px;'>
        <h3 style='color: #112D4E;'>ℹ️ About This App</h3>
        <p style='font-size: 16px; color: #333333;'>
            <strong>💡 Idea:</strong> This application helps you extract text from ID card images using modern OCR (Optical Character Recognition) technology. It's useful for digitizing printed information quickly and accurately.<br><br>

            <strong>⚙️ How It Works:</strong><br>
            - The image is processed using OpenCV.<br>
            - Tesseract OCR engine extracts text from the image.<br>
            - All detected lines are shown dynamically.<br><br>

            <strong>👨‍💻 Developed By:</strong> Mohamed Mostafa<br>
            Built with ❤️ using Python & Streamlit.
        </p>
    </div>
""", unsafe_allow_html=True)
