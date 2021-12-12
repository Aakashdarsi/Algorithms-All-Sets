import mysql.connector as m
mydb = m.connect()
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)