import requests

url = "http://localhost/api/auth"
api_payload = {"password": "P6EiId3_"}

try:
    r = requests.post(url, json=api_payload, timeout = 5)

    if r.status_code == 200:
        data = r.json()

        sid = data['session']['sid']
        print(f"Login Succesful! SID: {sid}")
        stats_url = "https://localhost/api/stats/summary"
        header = {"X-FTL-SID": sid}

        stats_r = requests.get(stats_url, headers=header)
        stats = stats_r.json()

        print(f"Ads Blocked Today: {stats['queries']['blocked']}")

    else:
        print(f"Server rejected login: {r.status_code}")

except KeyError as e:
    print(f"Response format error: Could not find key {e}")
    print(f"Full Response was: {r.text}")
except Exception as e:
    print(f"Unexpected error: {e}")