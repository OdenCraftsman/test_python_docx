import os
import docx

if __name__ == "__main__":
    file_name = os.path.splitext(__file__.split("\\")[-1])[0]

    doc = docx.Document()

    doc.add_picture("../assets/image/test_image.png", docx.shared.Mm(100))

    doc.save(f"../../test_output/{file_name}.docx")