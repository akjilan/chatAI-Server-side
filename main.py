from fastapi import FastAPI
from database.models import Base
from database.database import engine
from endpoints.upload import router as upload_router
from endpoints.get_pdfs import router as get_pdfs_router
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the server!"}

# Create database tables
Base.metadata.create_all(bind=engine)

# Register Routers
app.include_router(upload_router, prefix="/api")
app.include_router(get_pdfs_router, prefix="/api") 
