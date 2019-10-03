from configparser import ConfigParser

file = "TestData.ini"
config =  ConfigParser()
config.read(file)


val =config.get("TC004","url")
print(val)



config.add_section("TC002")
config.set("TC002","Password","passwoed#234")

with open(file, 'a') as configfile:
    config.write(configfile)