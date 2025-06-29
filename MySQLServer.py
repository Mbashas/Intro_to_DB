import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS alx_book_store")

print("Table created successfully!")

mycursor.close()
mydb.close()
