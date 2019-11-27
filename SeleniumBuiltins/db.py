import mysql.connector





def getEmpDetails(query):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin123",
            database="DemoBD"

        )
        mycursor = mydb.cursor()

        mycursor.execute(query)
        fetch = mycursor.fetchall()
        mydb.commit()
        for i in fetch:
            print(i)

def insertEmp(query):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin123",
            database="DemoBD"

        )
        mycursor = mydb.cursor()

        mycursor.execute(query)
        mydb.commit()



