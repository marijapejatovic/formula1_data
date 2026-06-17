import requests
r = requests.get('https://api.openf1.org/v1/weather?session_key=latest')
print(r.json()[0])