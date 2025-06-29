import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    
    if mydb.is_connected():
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
        mycursor.close()
        mydb.close()
    else:
        print("Error connecting to MySQL")
        
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
