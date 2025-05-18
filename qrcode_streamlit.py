import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import base64
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="QR Code Generator - PharmApp", layout="centered")

# --- LOAD LOGO ---
logo_path = os.path.join("assets", "nct_logo.png")
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

# --- SUBTITLE ---
st.markdown("### QR Code Generator for URLs", unsafe_allow_html=True)

# --- INPUT FORM ---
url = st.text_input("🔗 Enter URL to generate QR Code")

# --- GENERATE QR CODE ---
if url:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Hiển thị QR code
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Chuyển sang BytesIO để Streamlit chấp nhận
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    st.image(buffer, caption="Generated QR Code", use_column_width=False)


    # Save to buffer for download
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()

    # Download button
    b64 = base64.b64encode(img_bytes).decode()
    href = f'<a href="data:file/png;base64,{b64}" download="qrcode.png">📥 Download QR Code</a>'
    st.markdown(href, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""<br><hr><div style='text-align:center; font-size: 12px'>
| Copyright 2025 | 🧠 Nghiên Cứu Thuốc | PharmApp |<br>
| www.nghiencuuthuoc.com | Zalo: +84888999311 |
</div>""", unsafe_allow_html=True)
