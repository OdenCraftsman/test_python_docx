import os
import docx

from docx2pdf import convert

if __name__ == "__main__":
    file_name = os.path.splitext(__file__.split("\\")[-1])[0]

    converted_file_name = f"../../test_output/make_table.docx"

    doc = docx.Document(converted_file_name)

    # doc.add_paragraph("Hello world!")
    # doc.save(f"../../test_output/{file_name}.docx")

    convert(converted_file_name, f"../../test_output/{file_name}.pdf")