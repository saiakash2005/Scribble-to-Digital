from utils.ocr_processor import process_image_and_extract

def run_ocr(uploaded_file):
    """
    Handles OCR pipeline
    Image -> Preprocessing -> Text Extraction
    """

    try:
        text = process_image_and_extract(uploaded_file)

        if not text.strip():
            return "No text detected in image."

        return text

    except Exception as e:
        return f"OCR Error: {str(e)}"