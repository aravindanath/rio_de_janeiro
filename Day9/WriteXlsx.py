import openpyxl
# opnepyxl is the lib to read and write xlsx files..

path ="./TestData.xlsx"

op = openpyxl.load_workbook(path)

vk = op.sheetnames
print("No of sheets present in the workbook",vk)

# Wite to sheet
sh = op["DemoSheet"]
# Cell address is A1 --> 1st cell in the worksheet
sh["A1"]="Welcome to pyexl class"
sh["B10"]="Welcome to pyexl class"



op.save(path)