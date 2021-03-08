import requests
import json

url = "https://sandboxdnac.cisco.com:443/api/system/v1/auth/token"

payload  = {}
headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=',
  'port': '443'
}

response = requests.request("POST", url, headers=headers, data = payload)

token_dna=response.json()['Token']  #auth token
#print(response.text.encode('utf8'))
#print (token)



###get device list 

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload = {}
headers = {
  'x-auth-token': token_dna,
  'Cookie': 'JSESSIONID=sy9i2y36kwkg15kkuxdem26pt'
}

response = requests.request("GET", url, headers=headers, data = payload)
print("\n---------------------------------------")
print(response.text.encode('utf8'))


devs=response.json()
devs=devs['response'] ##??? formatting issues I guess
local_inv=[]
for dev in devs:
    info={
    "name":dev['hostname'],
    "type":dev['type'],
    "mac":dev['macAddress'], 
    "serial":dev['serialNumber'],
    "category":"DNAc"
    }
    local_inv.append(info)
print("\n----------------------")
print(local_inv)

with open('local_inv.json', 'w') as f:
    json.dump(local_inv, f)