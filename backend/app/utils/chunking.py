def chunk_resume(resume_text):
    """
    Split resume into logical sections
    """
    sections = resume_text.split("\n\n")  # simple split

    chunks = [s.strip() for s in sections if len(s.strip()) > 30]

    return chunks