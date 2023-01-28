// Copyright (c) 2022, DT team and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Stock Balance - Daily_2"] = {
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
