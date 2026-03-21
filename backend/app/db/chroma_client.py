import chromadb
from chromadb.config import Settings

# Initialize client
client = chromadb.Client(Settings(persist_directory="./chroma_db"))

# Create collection
collection = client.get_or_create_collection(name="resume_chunks")