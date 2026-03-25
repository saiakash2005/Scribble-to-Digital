from utils.ai_processor import process_text_with_ai

def run_ai_processing(ocr_text):
    """
    Sends OCR text to AI for:
    - Grammar correction
    - Sentence reconstruction
    - Task extraction
    """

    try:
        clean_text, tasks = process_text_with_ai(ocr_text)

        return {
            "clean_text": clean_text,
            "tasks": tasks
        }

    except Exception as e:
        return {
            "clean_text": "",
            "tasks": [],
            "error": f"AI Processing Error: {str(e)}"
        }