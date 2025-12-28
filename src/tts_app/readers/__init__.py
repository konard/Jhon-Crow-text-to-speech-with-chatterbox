"""Document readers for various file formats."""

from .base import DocumentReader
from .pdf_reader import PDFReader
from .docx_reader import DOCXReader
from .text_reader import TextReader
from .markdown_reader import MarkdownReader
from .registry import ReaderRegistry

__all__ = [
    "DocumentReader",
    "PDFReader",
    "DOCXReader",
    "TextReader",
    "MarkdownReader",
    "ReaderRegistry",
]
