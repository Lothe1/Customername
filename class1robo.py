import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gamz"
    )
print(mydb)

x="test"
while(x != "done"):
    x = input('Enter the platform:')
    mycursor = mydb.cursor()
    query = "select title, platform from gamz where platform = '"+x+"' order by title limit 5 ;"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
