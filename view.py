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

    sql = "SELECT * FROM nft_events ORDER BY timestamp ASC LIMIT 100"
    cursor.execute(sql)

    # Fetch all rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    sql = "SELECT COUNT(*) FROM nft_events"
    cursor.execute(sql)

    # Fetch all rows
    count = cursor.fetchone()[0]

    print("COUNT; ", count)

    cursor.close()
    # Close the connection when done
    connection.close()
    print("Connection closed")
