import frappe
from frappe.model.document import Document
from erpnext.selling.doctype.customer.customer import Customer

class Customer_xyz(Document):
    def after_insert(self):
        self.update_customer_group_count()

    def on_update(self):
         self.update_customer_group_count()

def update_customer_group_count(doc, method):
    print('asfafaf')
    if doc.customer_group:
        customer_count = frappe.db.count('Customer', filters={'customer_group': doc.customer_group})
        
        
        doc.custom_count = customer_count
        

