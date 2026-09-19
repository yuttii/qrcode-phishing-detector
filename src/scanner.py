import cv2

def get_qr_from_image(image_bgr):
    detector = cv2.QRCodeDetector()
    decoded_text, _, _ = detector.detectAndDecode(image_bgr)
    return decoded_text or None