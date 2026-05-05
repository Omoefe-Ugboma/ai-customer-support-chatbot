from PyPDF2 import PdfReader


def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return text


def extract_text_from_txt(file) -> str:
    return file.read().decode("utf-8")