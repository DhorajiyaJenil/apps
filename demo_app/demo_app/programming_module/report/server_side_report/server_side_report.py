# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

# import frappe

# def execute(filters=None):
#     if not filters: filters = {}

#     data, columns = [], []

#     columns = get_columns()
#     cs_data = get_cs_data(filters)

#     if not cs_data:
#         frappe.msgprint(_('No records found'))
#         return columns, cs_data

#     data = []
#     for d in cs_data:
#         row = frappe._dict({
#             'first_name': d.first_name,
#             'dob': d.dob,
#             'age': d.age
#         })
#         data.append(row)

#     return columns, data

# def get_columns():
#     return [
#         {
#             "fieldname": 'first_name',
#             "label": frappe._('Name'),  # Correct usage of frappe._() for translation
#             "fieldtype": 'Data',
#             "width": '120'
#         },
#         {
#             "fieldname": 'dob',
#             "label": frappe._('DOB'),
#             "fieldtype": 'Date',
#             "width": '120'
#         },
#         {
#             "fieldname": 'age',
#             "label": frappe._('Age'),
#             "fieldtype": 'Data',
#             "width": '100'
#         }
#     ]

# def get_cs_data(filters):
#     conditions = get_conditions(filters)
#     data = frappe.get_all(
#         doctype='server_side',
#         fields=['first_name', 'dob', 'age'],
#         filters=conditions,
#         order_by='first_name desc'
#     )
#     return data

# def get_conditions(filters):
#     conditions = {}
#     for key, value in filters.items():
#         if value:
#             conditions[key] = value

#     return conditions
