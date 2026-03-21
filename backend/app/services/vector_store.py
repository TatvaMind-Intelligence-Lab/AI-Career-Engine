from app.db.chroma_client import collection
from .embedding import get_embedding


def store_resume_chunks(chunks):
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"chunk_{i}"]
        )