# Copyright (c) 2024, D-codE and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class clientside(Document):
	pass

	@frappe.whitelist()
	def frappe_call(msg):
		import time
		time.sleep(5)
		frappe.msgprint(msg)

		


	  	return "hi this message from frm_call"
