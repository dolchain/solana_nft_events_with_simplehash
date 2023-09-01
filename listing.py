import json
import requests

url = "https://api.simplehash.com/api/v0/nfts/listing_events/solana?limit=2"

headers = {
    "accept": "application/json",
    "X-API-KEY": "victoriagu92_sk_474fed45-f38f-4eed-b615-d1055c4b669b_p3pvvtuochvjswwv"
}

response = requests.get(url, headers=headers)
data = json.loads(response.text)
count = 0

while data['next_cursor'] is not None:
    response = requests.get(data['next'], headers=headers)
    data = json.loads(response.text)
    
    count = count + 1
    print(count)
    if (count > 1):
        break
    # Code to execute while the condition is True

# print(response.text)
