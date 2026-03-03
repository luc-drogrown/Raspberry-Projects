import requests

api_payload = {"password": "P6EiId3_"}
server_cert_path = 'tls_ca.crt'
try:

    r = requests.request("POST",'https://localhost/api/auth', json=api_payload, verify=server_cert_path)
    data = r.json()
    print(f"Status: {data['status']}")
    r.text
except Exception as e:
    print(f"Connection failed: {e}")