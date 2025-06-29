import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

# Create database if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

print("Database 'alx_book_store' created successfully!")

mycursor.close()
mydb.close()
