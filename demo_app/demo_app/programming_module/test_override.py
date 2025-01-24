
import frappe
from frappe import _
from frappe.model.document import Document

class test_override(Document):
    def validate(self):
        frappe.throw("hellooooo")

