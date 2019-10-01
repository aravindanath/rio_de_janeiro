from datetime import datetime


dt = datetime.now()
print("Current date n time",dt)

currentDate =  str(dt).split(".")[0]
print(currentDate)


final= currentDate.replace("-","_").replace(":","_").replace(" ","_")
print("Demofile_"+final+".jpg")

