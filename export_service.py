from utils.file_export import export_txt, export_csv


def generate_txt(clean_text):

    try:
        path = export_txt(clean_text)
        return path

    except Exception as e:
        return f"TXT Export Error: {str(e)}"


def generate_csv(tasks):

    try:
        path = export_csv(tasks)
        return path

    except Exception as e:
        return f"CSV Export Error: {str(e)}"