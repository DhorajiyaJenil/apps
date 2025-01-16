import frappe
import string
import random

def all():
    pass

def cron():

    print("\n\nInserting a new one\n\n")

    letters = string.ascii_letters
    one = " ".join(random.choice(letters) for i in range(20))

    new_one = frappe.get_doc({
        "doctype": "One",
        "title": one
    })

    new_one.insert()
    frappe.db.commit()