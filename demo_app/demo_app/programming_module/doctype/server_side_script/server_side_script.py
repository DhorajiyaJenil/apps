# Copyright (c) 2024, D-codE and contributors
# For license information, please see license.txt

# import frappe
# from frappe import _
# from frappe.model.document import Document

# class serversidescript(Document):
#     def before_save(self):
#         self.calculate_percentage()  # Call the method correctly

#     def calculate_percentage(self):
#         total_marks = 0
#         max_marks = 0

#         # Assuming exam_scores is a child table in the document
#         for score in self.exam_scores:
#             total_marks += score.marks_obtained
#             max_marks += score.max_marks

#         if max_marks > 0:
#             percentage = (total_marks / max_marks) * 100
#         else:
#             percentage = 0

#         # Assign the calculated percentage to the document
#         self.percentage = percentage
#         self.save()  # Save the document after modification
