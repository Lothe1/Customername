from flask import Flask
app = Flask(__name__)


import mysql.connector
mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="",
    database="gamz"
    )
mycursor = mydb.cursor()

@app.route('/')
def hello():
    x=""
    query = "select * from customers"
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    for rows in result:
        x = x+str(rows)+"<br/>"             
    return x


if __name__ == "__main__":
    app.run()