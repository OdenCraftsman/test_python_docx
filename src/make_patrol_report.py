import os
from command.convert import save_docx_and_pdf

import docx

from constants.paths import PATHS
from command.make_header import make_header
from command.make_table import make_table_by_check_items


def make_patrol_report_docx(
    patrol_result_data:dict,
) -> docx.Document:
    doc = docx.Document()

    doc = make_header(
        doc,
        owner_name=patrol_result_data["owner_name"],
        property_name=patrol_result_data["property_name"],
    )

    doc = make_table_by_check_items(
        doc,
        check_items=patrol_result_data["check_items"],
    )

    return doc

if __name__ == "__main__":
    sample_data = {
        "owner_name" : "株式会社ドアーズ",
        "property_name" : "ドアーズマンション",
        "check_items": {
            "cleaning":[
                ["共用部清掃", True],
                ["ゴミステーション", True],
                ["駐輪場・駐車場清掃", False],
                ["建物外周部", False],
                ["除草作業", True],

            ],
            "checking":[
                ["内外壁", True],
                ["床", True],
                ["駐輪場", False],
                ["駐車場", True],
                ["外部収納", True],
                ["カーポート", False],
                ["ゴミステーション", True],
                ["集合ポスト", False],
                ["建物外周部", True],
                ["雑草駆除", False],
                ["その他の目視点検箇所（任意）", "ダミーテキスト。"*10],
                ["特記事項／報告事項", "ダミーテキスト。"*10],
            ],
        }
    }

    test_docx_file_name = "test_patrol_report.docx"
    test_docx_file_path = os.path.join(PATHS["test_output"], test_docx_file_name)

    test_pdf_file_name = "test_patrol_report.pdf"
    test_pdf_file_path = os.path.join(PATHS["test_output"], test_pdf_file_name)

    doc = make_patrol_report_docx(sample_data)
    save_docx_and_pdf(doc, test_docx_file_path, test_pdf_file_path)