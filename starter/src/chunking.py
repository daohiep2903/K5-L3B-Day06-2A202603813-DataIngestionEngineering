"""Deterministic chunking preserving source offsets and section boundaries."""
import hashlib
import re
from .models import Chunk


def _regions(page):
    text = page.text
    marks = list(re.finditer(r"^(\d+)(?:\.\d+)*\.  .+$", text, re.M))
    cuts = [0] + [m.start() for m in marks if m.start() and m.group(1) != page.metadata.get("top_level_section")]
    # Splitting at every numbered heading is shared by A/B/C and keeps labels accurate.
    cuts = sorted(set([0] + [m.start() for m in marks] + [len(text)]))
    section = page.metadata["top_level_section"]
    for start, end in zip(cuts, cuts[1:]):
        match = re.match(r"(\d+)(?:\.\d+)*\.  ", text[start:end])
        if match:
            section = match.group(1)
        yield start, end, section


def _chunk(page, start, end, section):
    while start < end and page.text[start].isspace():
        start += 1
    while end > start and page.text[end - 1].isspace():
        end -= 1
    if start == end:
        return None
    base = page.metadata["char_start"]
    content = page.text[start:end]
    key = f"{page.document_id}:{page.page}:{base+start}:{base+end}:{content}"
    metadata = dict(page.metadata, char_start=base+start, char_end_exclusive=base+end, top_level_section=section)
    return Chunk(hashlib.sha256(key.encode()).hexdigest(), page.document_id, page.source, page.page, content, metadata)


def fixed_size(page, size, overlap):
    if not 0 <= overlap < size:
        raise ValueError("Require 0 <= overlap < size")
    chunks = []
    for lo, hi, section in _regions(page):
        start = lo
        while start < hi:
            end = min(start + size, hi)
            chunk = _chunk(page, start, end, section)
            if chunk:
                chunks.append(chunk)
            if end == hi:
                break
            start = end - overlap
    return chunks


def by_paragraph(page, max_size):
    if max_size <= 0:
        raise ValueError("max_size must be positive")
    chunks = []
    for lo, hi, section in _regions(page):
        start = lo
        while start < hi:
            end = min(start + max_size, hi)
            if end < hi:
                boundary = page.text.rfind("\n\n", start, end)
                if boundary > start:
                    end = boundary + 2
            chunk = _chunk(page, start, end, section)
            if chunk:
                chunks.append(chunk)
            start = end
    return chunks
