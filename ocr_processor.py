import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def process_image_and_extract(uploaded_file):

    try:
        uploaded_file.seek(0)

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

        # check empty buffer
        if len(file_bytes) == 0:
            return None, "Uploaded file is empty."

        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return None, "Unable to read image file."

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Noise removal
        blur = cv2.GaussianBlur(gray, (5,5), 0)

        # Threshold
        thresh = cv2.threshold(
            blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        text = pytesseract.image_to_string(thresh)

        return text, None

    except Exception as e:
        return None, str(e)