from configparser import ConfigParser

ini = ConfigParser()
ini["TC004"]={'url':'https://www.flipkart.com'
              ,'user':'shobin','password':'password!23'}

with open('./TestData.ini', 'a') as tmp:
       ini.write(tmp)