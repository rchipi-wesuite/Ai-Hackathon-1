﻿from pypdf import PdfReader


def load_pdf_text(file_path: str) -> str:
    """Extract text from a PDF."""
    try:
        reader = PdfReader(file_path)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return ""

