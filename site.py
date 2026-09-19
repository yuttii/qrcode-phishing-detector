import streamlit as st
import cv2
import numpy as np
from src.scanner import get_qr_from_image

# Page configuration
st.set_page_config(
    page_title="Phishing QR Code Detector",
    layout="centered"
)

st.title("Phishing QR Code Detector")
st.write("Upload an image with a QR code to check its safety.")

# File upload via web interface
uploaded_file = st.file_uploader("Select a QR code file (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert image for OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Convert to RGB for display in Streamlit
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    st.image(image_rgb, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Searching and analyzing QR code..."):
        url = get_qr_from_image(image_bgr)

    if url is None:
        st.error("Failed to detect or decode a QR code in this image.")
    else:
        st.success("QR code successfully decoded!")
        st.code(url, language="text")

        # --- Security check logic ---
        st.subheader("Security Check Results:")
        
        dangerous_keywords = ["login", "verify", "update", "account", "secure", "free", "bonus"]
        suspicious_tlds = [".xyz", ".top", ".gq", ".ml", ".tk", ".cf"]
        
        is_suspicious = any(keyword in url.lower() for keyword in dangerous_keywords)
        has_bad_tld = any(url.lower().endswith(tld) for tld in suspicious_tlds)
        
        if "http://" in url:
            st.warning("Warning: The link uses an unencrypted HTTP protocol.")
        
        if is_suspicious or has_bad_tld:
            st.error("Dangerous! Phishing indicators detected (suspicious keywords or domain).")
        elif not is_suspicious and "https://" in url:
            st.success("Safe: The link is secure and shows no obvious threats.")
        else:
            st.info("Neutral: The link appears normal, but remain vigilant.")