from fastapi import APIRouter, UploadFile, File , Depends
from services.pdf_service import save_pdf_to_db
from utils.pdf_utils import extract_text_from_pdf
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/upload-pdf/")
async def upload_pdfs(files: list[UploadFile] = File(...)):
    responses = []

    for file in files:
        pdf_content = file.file.read() 
        binary_content = await file.read()  # Read binary content of the file
        pdf_text = extract_text_from_pdf(file.file)  # Extract text from uploaded PDF

        # Save the extracted text, filename, and binary content to the database
        save_pdf_to_db(file_data=pdf_text, filename=file.filename, binary_data=pdf_content )  

        responses.append({
            "filename": file.filename,
            "status": "saved"
        })

    return {"uploaded_files": responses}


