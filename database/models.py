from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, LargeBinary

Base = declarative_base()

class PDFFile(Base):
    __tablename__ = "pdf_files_second"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, nullable=False) # Store extracted PDF text
    binary_content = Column(LargeBinary)  # Store binary content of the file
