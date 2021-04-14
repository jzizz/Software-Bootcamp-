import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": ""
}

response = requests.request('GET', url, headers=headers, data = payload)
orgs=response.json()
for org in orgs:
    print("ID is " + str(org['id'])+ " name is " + str(org['name'])) 

