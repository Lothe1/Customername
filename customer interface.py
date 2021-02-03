import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="",
    database="gamz"
    )

mycursor = mydb.cursor()

def createTable():
    mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
createTable()

def insertCustomer(name, address):
    sql="INsert into customers(name,address) values (%s,%s)"
    val=(name, address)
    mycursor.execute(sql,val)
    mydb.commit()
    
    print(mycursor.rowcount, "records inserted.")
    
def printtable():
    query = "select * from customers"
    mycursor.execute(query)
    result = mycursor.fetchall()
    for row in result:
        print(row)

def Addcustomers():
    name = input('Enter the name of customer:')
    if name != "none":
        address = input('Enter the address:')
        query = "select count(*) from customers where name like '{}' and address like '{}';".format(name,address)
        mycursor.execute(query)
        result = mycursor.fetchall()
        count = result[0][0]
        if count==0 :
            insertCustomer(name, address)
            Addcustomers()
            mydb.commit()
    
        
def Updatecustomers():
    cusid = input('enter id: ')
    query = "select * from customers where id like '{}';".format(cusid);
    mycursor.execute(query)
    result = mycursor.fetchall()
    print(result)
    name = input('Enter the new name of customer:')
    address = input('Enter the new address:')
    
    query = "UPDATE customers SET name = '{}', address = '{}' where id like '{}'".format(name,address,cusid);
    mycursor.execute(query)
    mydb.commit()
    
    
def removecustomers():
    cusid = input('enter id: ')
    query="DELETE from customers where id like '{}';".format(cusid);
    mycursor.execute(query)
    mydb.commit()
    
while True:
    printtable()
    print("What do you wanna do")
    print("1.Add customers")
    print("2.Update customers")
    print("3.Removecustomers")
    x =input('enter: ')
    
    if x =="1":
        Addcustomers()
    elif x=="2":
        Updatecustomers()
    elif x=="3":
        removecustomers()
    
    