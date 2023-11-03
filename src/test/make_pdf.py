import os
import docx

from docx2pdf import convert

if __name__ == "__main__":
    file_name = os.path.splitext(__file__.split("\\")[-1])[0]

    doc = docx.Document()

    doc.add_paragraph("Hello world!")

    doc.save(f"../../test_output/{file_name}.docx")
    convert(f"../../test_output/{file_name}.docx", f"../../test_output/{file_name}.pdf")