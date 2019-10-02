car={"make":"honda", "model":"city", "year":"2018"}
print(car)
try:
    x=car["color"]
    print(x)
except:
    print("colour not found")
finally:
    print("try with a valid key value")