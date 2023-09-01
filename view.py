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
    cursor = connection.cursor()

    # Perform database operations here

    sql = "SELECT * FROM nft_events"
    cursor.execute(sql)

    # Fetch all rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    # Close the connection when done
    connection.close()
    print("Connection closed")
