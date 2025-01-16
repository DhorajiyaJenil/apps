# Copyright (c) 2025, dcode and contributors
# For license information, please see license.txt



import frappe
from frappe.model.document import Document

class practicedoc(Document):
    def before_save(self):
        calculate_marks(self)

def calculate_marks(doc):
    """
    Calculate total marks and percentage based on the child table data.
    """
    total_marks_obtained = 0
    total_maximum_marks = 0

    for row in doc.subject_marks:
        try:
            marks_obtained = float(row.marks_obtained) if row.marks_obtained else 0
            maximum_marks = float(row.maximum_marks) if row.maximum_marks else 0

            total_marks_obtained += marks_obtained
            total_maximum_marks += maximum_marks
        except ValueError:
            frappe.throw(f"Invalid marks or maximum marks in row: {row.idx}")

    if total_maximum_marks > 0:
        percentage = (total_marks_obtained / total_maximum_marks) * 100
    else:
        percentage = 0

    doc.total_marks = total_marks_obtained
    doc.maximum_marks = total_maximum_marks
    doc.percentage = percentage

@frappe.whitelist()
def on_update(doc_name):
    """
    Recalculate marks and percentage when the document is updated.
    """
    doc = frappe.get_doc("practicedoc", doc_name)

    calculate_marks(doc)
    doc.save()

