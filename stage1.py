import requests
import json
organizationId=549236

#------get network id

url = "https://api.meraki.com/api/v1/organizations/549236/networks"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": ""
}

response = requests.request('GET', url, headers=headers, data = payload)
nets=response.json()
for net in nets:
    if net['name'] == "DevNet Sandbox ALWAYS ON":
        networkId=net['id']



url = "https://api.meraki.com/api/v1/organizations/549236/devices"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": ""
}

response = requests.request('GET', url, headers=headers, data = payload)

devs=response.json()
local_inv=[]
for dev in devs:
    if dev['networkId'] == networkId:
        info={
        "name":dev['name'],
        "type":dev['model'],
        "mac":dev['mac'], 
        "serial":dev['serial']
        }
        local_inv.append(info)
print(local_inv)

##write to file 

with open('local_inv.json', 'w') as f:
    json.dump(local_inv, f)
#print(response.text.encode('utf8'))
