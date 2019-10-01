print("Starting....")

try:
    i =10;
    z =0;
    print(i/z)

except FileNotFoundError:
    print("message")
except ZeroDivisionError:

    print("message zero")
    # raise Exception("DEMO EXCEPTION..")
except:
    print("Msg")
else:
    print("Else block will execute..")
finally:

    print("DB closing...")
print("ending....")
