import mysql.connector

# Configure the database connection
config = {
    "user": "root",
    "password": "q1w2E#R$",
    "host": "localhost",
    "database": "solana_nft"
}

# Establish the connection
connection = mysql.connector.connect(**config)

if connection.is_connected():
    print("Connected to MySQL database")

    # Perform database operations here

    # Close the connection when done
    connection.close()
    print("Connection closed")
