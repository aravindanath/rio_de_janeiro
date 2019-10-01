
def exception():
    try:
        car = {"make": "bmw", "Model": '550i', 'year': 2019}
        print(car["colour"])
    except:
        print("Colour not found")
    # raise exception()


exception()