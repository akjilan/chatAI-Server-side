from database.database import SessionLocal
from database.models import PDFFile


def save_pdf_to_db(file_data: str, filename: str, binary_data: bytes):
    db = SessionLocal()
    pdf_entry = PDFFile(filename=filename, content=file_data, binary_content=binary_data)
    db.add(pdf_entry)
    db.commit()
    db.refresh(pdf_entry)
    db.close()
    return pdf_entry




# Function to fetch all stored PDFs
def get_all_pdfs():
    db = SessionLocal()
    pdf_entries = db.query(PDFFile).all()
    db.close()
    return pdf_entries
