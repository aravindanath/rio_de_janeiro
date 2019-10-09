import openpyxl

path = "./TestData.xlsx"
# Path for the xlsx workbook

# Load workbook
op = openpyxl.load_workbook(path)

op.create_sheet("DemoSheet",3)
# Save will save the updateds
op.save(path)