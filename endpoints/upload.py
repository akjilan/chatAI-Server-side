from fastapi import APIRouter, UploadFile, File , Depends
from services.pdf_service import save_pdf_to_db
from utils.pdf_utils import extract_text_from_pdf
from sqlalchemy.orm import Session


router = APIRouter()


# @router.post("/upload-pdf/")
# async def upload_pdfs(files: list[UploadFile] = File(...)):
#     responses = []

#     for file in files:
#         pdf_content = file.file.read() 
#         binary_content = await file.read()  # Read binary content of the file
#         pdf_text = extract_text_from_pdf(file.file)  # Extract text from uploaded PDF

#         # Save the extracted text, filename, and binary content to the database
#         save_pdf_to_db(file_data=pdf_text, filename=file.filename, binary_data=pdf_content )  

#         responses.append({
#             "filename": file.filename,
#             "status": "saved"
#         })

#     return {"uploaded_files": responses}


#     @router.post("/upload-pdf/")
# async def upload_pdf(files: list[UploadFile] = File(...)):
#     for file in files:
        
#         contents = await file.read()
#         save_pdf_to_db(file_data=pdf_text, filename=file.filename, binary_data=pdf_content )  
#         # Process each file
#         print(f"Uploaded file: {file.filename}, size: {len(contents)} bytes")
#     return {"message": f"Uploaded {len(files)} file(s) successfully"}


@router.post("/upload-pdf/")
async def upload_pdf(files: list[UploadFile] = File(...)):
    for file in files:
        # Read the binary content of the file
        binary_content = await file.read()      
        # Save the file data to the database
        save_pdf_to_db( filename=file.filename, binary_data=binary_content)
        
        print(f"Uploaded and saved file: {file.filename}")
        
    return {"message": f"Uploaded and saved {len(files)} file(s) successfully"}


