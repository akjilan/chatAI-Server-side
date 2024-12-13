from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your PostgreSQL credentials
DATABASE_URL = "postgresql+psycopg2://postgres:@localhost/pdf_db"

# Create the database connection engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
