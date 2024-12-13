from fastapi.responses import StreamingResponse
from io import BytesIO
from database.models import PDFFile
from database.database import SessionLocal
from fastapi import APIRouter

router = APIRouter()

# Function to fetch PDF entries from the database
def get_all_pdfs():
    db = SessionLocal()
    pdf_entries = db.query(PDFFile).all()
    db.close()
    return pdf_entries

@router.get("/get-pdfs/")
async def get_pdfs():
    pdf_entries = get_all_pdfs()  # Fetch all PDF entries
    
    # Format the response
    result = [
        {"id": entry.id, "filename": entry.filename}
        for entry in pdf_entries
    ]
    
    return {"pdf_files": result}


@router.get("/get-pdf/{pdf_id}")
async def get_pdf_by_id(pdf_id: int):
    db = SessionLocal()
    pdf_entry = db.query(PDFFile).filter(PDFFile.id == pdf_id).first()
    db.close()
    
    if not pdf_entry or not pdf_entry.binary_content:
        return {"detail": "PDF not found or has no binary content"}
    
    # Stream the binary content as a PDF
    pdf_stream = BytesIO(pdf_entry.binary_content)
    return StreamingResponse(pdf_stream, media_type="application/pdf", headers={
        "Content-Disposition": f"inline; filename={pdf_entry.filename}"
    })

