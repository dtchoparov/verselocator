import requests
import json

headers = {"api-key": "61b9891fb7e0ce510a7343153caaa402"}
response = requests.get("", headers=headers)

bibles = json.loads(response.text)

print(bibles["data"][0]["abbreviation"])
