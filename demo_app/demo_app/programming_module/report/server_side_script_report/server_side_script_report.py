# Copyright (c) 2025, dcode and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint

def execute(filters=None):
    if not filters:
        filters = {}

    data, columns = [], []
    columns = get_columns()
    cs_data = get_cs_data(filters)
    
    if not cs_data:
        msgprint(_('No record found'))
        return columns, cs_data

    data = []
    for d in cs_data:
        row = {
            'first_name': d.first_name,
            'dob': d.dob,
            'age': d.age
        }    
        data.append(row)
        
        chart = get_chart_data(data)
        message = None
        # print(chart)
        report_summary = None
    return columns, data , message , chart , report_summary

def get_columns():
    return [
        {
            'fieldname': 'first_name',
            'label': ('Name'),
            'fieldtype': 'Data', 
            'width': '120'
        },
        {
            'fieldname': 'dob',
            'label': ('DOB'),
            'fieldtype': 'Date', 
            'width': '120' 
        },
        {
            'fieldname': 'age',
            'label': ('Age'),
            'fieldtype': 'Int', 
            'width': '120'
        }
    ]

def get_cs_data(filters):
    conditions = get_conditions(filters)
    data = frappe.get_all(
        doctype='server side',
        fields=['first_name', 'dob', 'age'],
        filters=conditions,
        order_by='first_name desc'
    )
    return data

def get_conditions(filters):
    conditions = {}
    for key, value in filters.items():
        if filters.get(key):
            conditions[key] = value
    
    return conditions

def get_chart_data(data):
    if not data or len(data) == 0:
        return None

    labels = ['Age <= 50', 'Age > 50']
    
    age_data = {
        'Age > 50': 0,
        'Age <= 50': 0,
    }
    datasets = []
    
    for entry in data:
        if entry['age'] <= 50:
            age_data['Age <= 50'] += 1
        else: 
            age_data['Age > 50'] += 1
    
    datasets.append({
        'name': 'Age Status',
        'values': [age_data.get('Age <= 50', 0), age_data.get('Age > 50', 0)]
    })
    
    chart = {
        'data': {
            'labels': labels,
            'datasets': datasets
        },
        'type': 'bar',
        'height': 200,
    }
    # print(chart)
    return chart

