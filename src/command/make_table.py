import os
from typing import Literal

import docx
from docx.shared import Mm
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

ROW_HIGHT = Mm(8)

def make_table_by_check_items(
    doc:docx.Document,
    check_items:dict,
)->docx.Document:
    for table_type, data in check_items.items():
        table = doc.add_table(rows=0, cols=0, style="Table Grid")
        label_row(table, table_type=table_type)
        for i, list in enumerate(data):
            if type(list[-1]) != bool:
                break
            table.add_row().height = ROW_HIGHT
            table.rows[-1].cells[0].text = str(i+1)
            table.rows[-1].cells[1].text = list[0]
            table.rows[-1].cells[2].text = ""
            table.rows[-1].cells[3].text = "済" if list[1] else ""
    return doc


def label_row(
    table:docx.table.Table,
    table_type:Literal["cleaning","checking"] = "cleaning",
) -> None:
    label_text = {
        "cleaning" : ["", "巡回清掃", "作業内容", "実施"],
        "checking" : ["", "目視点検", "点検箇所", "実施"],
    }
    table.add_column(Mm(10))
    table.add_column(Mm(40))
    table.add_column(Mm(90))
    table.add_column(Mm(20))
    table.add_row().height = ROW_HIGHT
    for i, cell in enumerate(table.rows[0].cells):
        cell.text = label_text[table_type][i]
        _set_cell_background_color(cell, "C"*6)



def _set_cell_background_color(cell, color):
    shading_elm = parse_xml(r'<w:shd {} w:fill="{}"/>'.format(nsdecls('w'), color))
    cell._tc.get_or_add_tcPr().append(shading_elm)