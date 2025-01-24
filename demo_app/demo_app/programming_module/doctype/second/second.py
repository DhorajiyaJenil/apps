# Copyright (c) 2024, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

 class second(Document):
#     def validate(self):
#         frappe.throw('This is an error message')

#     # Properly indented method inside the class
#     def fetch_second_doctype_records(self):
#         # Fetch records from 'Second Doctype' with selected fields
#         records = frappe.db.get_list('Second Doctype', fields=['Name', 'Student Id'])
#         return records

 
# class second(Document):
#     def fetch_second_doctype_field(self):
#         # Fetch the 'Name' field of the first document in the 'Second Doctype'
#         name = frappe.db.get_value('Second Doctype', {'field_name': 'value_to_filter_by'}, 'Name')
#         return name

#     def fetch_multiple_fields(self):
#         # Fetch 'Name' and 'Student Id' from the 'Second Doctype'
#         result = frappe.db.get_value('Second Doctype', {'field_name': 'value_to_filter_by'}, ['Name', 'Student Id'], as_dict=True)
#         return result
