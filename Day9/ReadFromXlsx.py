import openpyxl
"""
https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/
"""
path= "./TestData.xlsx"

op = openpyxl.load_workbook(path)
ac = op.active

var = ac.cell(row=10,column=2)
print(var.value)
