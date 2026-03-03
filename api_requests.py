import requests

auth = "P6EiId3_"
r = requests.get('https://localhost/api/stats/summary&auth={auth}')
data = r.json()
print(f"Status: {data['status']}")
r.text