import mysql.connector
import json
import requests

url = "https://api.simplehash.com/api/v0/nfts/listing_events/solana?limit=50"

headers = {
    "accept": "application/json",
    "X-API-KEY": "victoriagu92_sk_474fed45-f38f-4eed-b615-d1055c4b669b_p3pvvtuochvjswwv"
}

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

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    sql = "INSERT INTO nft_events (nft_id, marketplace_id, event_type, from_address, to_address, total_price, timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    while data['next_cursor'] != None:
        print(data['next_cursor'])

        response = requests.get(data['next'], headers=headers)
        data = json.loads(response.text)
        for event in data['events']:
            # Perform database operations here
            if event['event_type'] == 'listing_added':
                values = (
                    event['nft_id'],
                    event['marketplace_id'],
                    event['event_type'],
                    event['seller_address'],
                    None,
                    event['price'],
                    event['listing_timestamp'].replace(
                        "T", " ").replace("Z", ""),
                )
                cursor.execute(sql, values)
                connection.commit()

    # Close the connection when done
    cursor.close()
    connection.close()
    print("Connection closed")
