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

    sql = "INSERT INTO nft_events (nft_id, marketplace_id, event_type, from_address, to_address, total_price, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (
        "solana.7Th9kACc3NJpk1W2XFuySinP2fbusfQpAahF6pkcXkTn",
        "tensor",
        "listing_added",
        "41v61wDUJALFLyspRwBhdLdDAZfdGZQ8cNDSkj3D5NkS",
        "BseDq2UHqYEqAAUm8c9UixYu97dedENzZ9v6JWTMYAhM",
        610000,
        "2023-09-01 20:23:08"
    )

    cursor.execute(sql, values)
    connection.commit()

    # Close the connection when done
    cursor.close()
    connection.close()
    print("Connection closed")
