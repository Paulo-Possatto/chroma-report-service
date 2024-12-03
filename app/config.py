import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "chroma_data")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "analysis_data")
