# demo_app/programming_module/events.py
import frappe
from frappe import _

def validate(doc, method):
    total_marks = 0
    marks_obtained = 0

    # Check if the 'subject' child table is populated
    if not doc.subject:
        frappe.throw(_("No marks data found for the student"))

    # Loop through the 'subject' child table to calculate the total marks and obtained marks
    for row in doc.subject:
        if not row.total_marks or not row.marks_obtained:
            frappe.throw(_("Missing marks data for a subject"))
        total_marks += row.total_marks
        marks_obtained += row.marks_obtained

    # Calculate the percentage if total marks are available
    if total_marks > 0:
        percentage = (marks_obtained / total_marks) * 100
        doc.percentage = percentage
    else:
        doc.percentage = 0  # If no total marks, set percentage to 0

    # Determine the status based on the percentage
    if doc.percentage < 33:
        doc.status = "Failed"
    elif 33 <= doc.percentage <= 50:
        doc.status = "Pass"
    else:
        doc.status = "Excellent"
    
    # Optionally log the status and percentage for debugging
    frappe.log_error(f"Updated Status: {doc.status}, Percentage: {doc.percentage}", "Student Validation")
