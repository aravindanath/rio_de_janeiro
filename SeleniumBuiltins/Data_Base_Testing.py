import mysql.connector



"""
Study material for python mysql

Need to add 'mysql-connector' pkg using PIP

https://pynative.com/python-mysql-database-connection/


"""

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin123",
  database="DemoBD"
)

mycursor = mydb.cursor()

# mycursor.execute("show databases")
getquery = "SELECT * from Employee;"
insertQuery ="INSERT INTO Employee  VALUES (1003, 'Arundathi', 'nath', 'Delhi','Bangalore','Python');"


get = True

if get == True:
    mycursor.execute(getquery)
    fetch = mycursor.fetchall()
    mydb.commit()
    for i in fetch:
        print(i)
else:
    mycursor.execute(insertQuery)
    mydb.commit()

# for i in mycursor:
#     print(i)



