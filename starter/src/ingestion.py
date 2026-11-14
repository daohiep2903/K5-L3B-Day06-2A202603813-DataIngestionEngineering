"""Document extraction with explicit empty-page warnings."""
import logging
import re
import unicodedata
from .models import DocumentPage


def normalize_text(text):
    text = unicodedata.normalize("NFC", text).replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[^\S\n]+", " ", text)
    return re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", text).strip()


def load_pdf(path, document_id, source):
    from pypdf import PdfReader
    pages = []
    for number, page in enumerate(PdfReader(path).pages, 1):
        text = normalize_text(page.extract_text() or "")
        if not text:
            logging.warning("Empty PDF page: %s page %s; OCR may be required", source, number)
        pages.append(DocumentPage(document_id, source, number, text))
    return pages
