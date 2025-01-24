# Copyright (c) 2025, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


# Rename a document in the "console" DocType from "CON00002" to "CON00003"
frappe.rename_doc('console', 'CON00002', 'CON00003')




