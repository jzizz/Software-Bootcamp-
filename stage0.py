import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data = payload)
orgs=response.json()
for org in orgs:
    print("ID is " + str(org['id'])+ " name is " + str(org['name'])) 

#------------------------------
print("\n")

organizationId=549236
url = "https://api.meraki.com/api/v1/organizations/{organizationId}/devices"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data = payload)

#devs=response.json()
#for dev in devs:
    #print("ID is " + str(org['id'])+ " name is " + str(org['name'])) 

#print(response.text.encode('utf8'))
#print(response.text.encode('utf8'))