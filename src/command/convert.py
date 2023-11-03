import docx
from docx2pdf import convert

def save_docx_and_pdf(
    docx: docx.Document,
    docx_file_path: str,
    pdf_file_path: str,
) -> None:
    docx.save(docx_file_path)
    convert(docx_file_path, pdf_file_path)