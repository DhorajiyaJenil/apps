# Copyright (c) 2024, D-codE and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document


class Student(Document):
    def on_update(self):
        self.calculate_percentage()

    def calculate_percentage(self):
        total_marks = 0
        total_max_marks = 0
        
        
        for mark in self.get('marks'):
            total_marks += mark.mark
            total_max_marks += mark.max_mark
        
        
        if total_max_marks > 0:
            percentage = (total_marks / total_max_marks) * 100
        else:
            percentage = 0
        
        
        self.percentage = percentage

        
        self.save()


	 
