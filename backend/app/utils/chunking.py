import re

SECTION_HEADERS = [
    "skills",
    "technical skills",
    "experience",
    "work experience",
    "professional experience",
    "projects",
    "education",
    "certifications",
    "summary",
    "objective"
]


def is_section_header(line):
    line = line.strip().lower()

    # strict match (not substring)
    return any(line == header or line.startswith(header + ":") for header in SECTION_HEADERS)


def detect_sections(text):
    lines = text.split("\n")

    sections = {}
    current_section = "general"
    sections[current_section] = []

    for line in lines:
        clean_line = line.strip().lower()

        if is_section_header(clean_line):
            current_section = clean_line
            sections[current_section] = []
        else:
            sections[current_section].append(line)

    # join
    for key in sections:
        sections[key] = "\n".join(sections[key]).strip()

    return sections


def split_into_subchunks(text, max_length=400):
    """
    Split long sections into smaller chunks
    """
    lines = text.split("\n")
    chunks = []
    current_chunk = []

    for line in lines:
        current_chunk.append(line)

        if len(" ".join(current_chunk)) > max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


def chunk_resume(resume_text):
    sections = detect_sections(resume_text)

    chunks = []

    for section, content in sections.items():
        if len(content) < 40:
            continue

        subchunks = split_into_subchunks(content)

        for sub in subchunks:
            chunk = f"[{section.upper()}]\n{sub}"
            chunks.append(chunk)

    return chunks