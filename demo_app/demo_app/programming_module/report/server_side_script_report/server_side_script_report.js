// Copyright (c) 2024, D-codE and contributors
// For license information, please see license.txt

frappe.query_reports["server side script report"] = {
	"filters": [
		{
            "fieldname": "name",
            "label": ("Server Side"),
            "fieldtype": "Link",  // fieldtype should be lowercase
            "options": "server side"  // Link to the DocType Server Side Scripting
        },
        {
            "fieldname": "dob",
            "label": ("DOB"),
            "fieldtype": "Date"  // Correct fieldtype for Date
        },
        {
            "fieldname": "age",
            "label": ("Age"),
            "fieldtype": "Int"  // Correct fieldtype for Integer
        }

	]
};
