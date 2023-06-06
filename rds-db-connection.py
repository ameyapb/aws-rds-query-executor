import mysql.connector
from getpass import getpass

host = input("Enter the host: ")
user = input("Enter the username: ")
dbname = input("Enter the database name: ")

# Get the password securely
password = getpass("Enter the password: ")

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = dbname
)

# Create a cursor object
cursor = cnx.cursor()

# Select all rows from the 'users' table
query = "SELECT * FROM users"
cursor.execute(query)

# Fetch all rows and print the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
cnx.close()
