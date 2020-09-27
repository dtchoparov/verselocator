import requests
import json
import api_key

headers = api_key.api_key
response = requests.get("", headers=headers)

bibles = json.loads(response.text)

print(bibles["data"][0]["abbreviation"])
