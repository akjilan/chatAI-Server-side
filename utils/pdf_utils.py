from PyPDF2 import PdfReader


def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text() or ""
    return pdf_text
