import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="bhavya")
mycursor=db.cursor()
mycursor.execute("Show databases")
mycursor.execute("select * from bhavya")
for i in mycursor:
	print(i)
