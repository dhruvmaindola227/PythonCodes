import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "I@mnewdhruv22",
    database = "coursesapi"
)

myCursor = mydb.cursor()

myCursor.execute("SELECT * FROM tables")

myResult = myCursor.fetchall()
for x in myResult:
    print(x)

