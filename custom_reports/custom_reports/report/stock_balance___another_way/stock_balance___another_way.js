// Copyright (c) 2023, DT team and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Stock Balance - another way"] = {
	"filters": [
		{
			"fieldname": "Item",
			"label": "Item Name",
			"fieldtype": "Link",
			"options": "Item"
		},
		{
			"fieldname": "St_Date",
			"label": "start_date",
			"fieldtype": "Date"
		},
		{
			"fieldname": "Ed_Date",
			"label": "end_date",
			"fieldtype": "Date"
		
		}

	]
};
