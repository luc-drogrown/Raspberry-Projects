import requests

r = requests.get('https://pi.hole/api/stats/summary')
r.text