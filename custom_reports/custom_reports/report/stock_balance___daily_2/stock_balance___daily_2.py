# Copyright (c) 2022, DT team and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	date = get_date()
	data = cumulate_data(data,date)
	return columns, data

# SLE = frappe.get_all(
# 	doctype = "Stock Ledger Entry",
# 	fields = ['item_code', 'warehouse','posting_date','voucher_type','company','actual_qty'],
# 	order_by = 'posting_date asc',
# 	filters=[['posting_date', 'between', ['2022-12-05', '2022-12-28']]]
	
# 	)

def get_columns(filters):
	columns = [
		{
			"label": ("Item"),
			"fieldname": "item_code",
			"fieldtype": "Link",
			"options": "Item",
			"width": 100,
		},
		{
			"label": ("Company"), 
			"fieldname": "company", 
			"width": 150
			
		},
		{
			"label": ("Warehouse"),
			"fieldname": "warehouse",
			"fieldtype": "Link",
			"options": "Warehouse",
			"width": 200,
		},
        
	]

	SLE = frappe.get_all(
	doctype = "Stock Ledger Entry",
	fields = ['item_code', 'warehouse','posting_date','voucher_type','company','actual_qty'],
	order_by = 'posting_date asc',
	filters=[['posting_date', 'between', [str(filters.get("St_Date")), str(filters.get("Ed_Date"))]]]
	
	)
	
	# for date in range(1,31):
	# 	col_date = {
	# 		"label":("Day_"+ str(date)) ,
	# 		"fieldname":("day_"+ str(date)),
	# 		"fieldtype": "Data",
	# 		"width" : 150,
	# 	}
	# 	columns.append(col_date)

	for d in SLE:
		col_date = {
			"label" : str(d.posting_date),
			"fieldname": str(d.posting_date),
			"fieldtype": "Data",
			"width" : 100,
		}
		for c in columns:
			flag = 0
			if c["label"] == col_date["label"]:
				flag = 1
		if flag ==  0:
			columns.append(col_date)
	
	temp = {
		'label': ("temp"),
		'fieldname': "temp",
		'fieldtype': 'data',
		'width': 150,
	}
	columns.append(temp)


	return columns

def get_data(filters):
	
	data =[]
	date =[]
	date = get_date()
	i = 0

	SLE = frappe.get_all(
	doctype = "Stock Ledger Entry",
	fields = ['item_code', 'warehouse','posting_date','voucher_type','company','actual_qty','qty_after_transaction'],
	order_by = 'posting_date asc',
	filters=[['posting_date', 'between', [str(filters.get("St_Date")), str(filters.get("Ed_Date"))]]]
	
	)

	
	for d in SLE:
		# day = str(int((str(d.posting_date))[8:]))
		row = {
			'item_code': d.item_code,
			'company': d.company,
			'warehouse': d.warehouse,
			# ('day_'+ day): d.actual_qty,
			str(d.posting_date): d.actual_qty
		}
		flag = 1
		
		for dic in data:       
			if (row["item_code"] == dic["item_code"]) & (row["warehouse"] == dic["warehouse"]) & (row["company"] == dic["company"]):
				flag = 0
				if str(d.posting_date) not in dic.keys():
					dic[str(d.posting_date)] = row[str(d.posting_date)]
				else:
					dic[str(d.posting_date)] += row[str(d.posting_date)]
		
		# if i > (len(date)-1):
		# 	row['temp'] = 0
		# else:
		# 	row['temp'] = filters.get("St_Date")
		# i +=1
		
		if flag == 1:
			data.append(row)
						
	return data

def get_date():
	date_list= frappe.db.get_list('Stock Ledger Entry', pluck='posting_date')
	date_list = list(set(date_list))
	date_list.sort()
	new_date = []
	for d in date_list:
		x = str(d)
		new_date.append(x)
	return new_date


def cumulate_data(data,ls_date):
	sum = 0
	r = len(ls_date)
	for dict in data:
		if ls_date[0] not in dict.keys():
			dict[ls_date[0]] = 0

		for i in range(1,r):
			if ls_date[i] not in dict.keys():
				dict[ls_date[i]] = dict[ls_date[i-1]]
			else:
				dict[ls_date[i]] += dict[ls_date[i-1]]
	return data