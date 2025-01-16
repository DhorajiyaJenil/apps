import frappe
import logging

# Create a logger
logger = logging.getLogger(__name__)

@frappe.whitelist()
def update_customer_group_count(doc, method):
    if doc.customer_group:
        # Query to count the number of customers in the selected customer group
        customer_count = frappe.db.count('Customer', filters={'customer_group': doc.customer_group})
        
        # Log the customer group and the count
        logger.info(f"Customer Group: {doc.customer_group}, Count: {customer_count}")
        
        # Set the customer group count field
        doc.customer_group_count = customer_count
        doc.save()  # Save the updated count field to the database
    else:
        logger.info(f"No customer group selected for {doc.customer_name}")
    
    return doc

