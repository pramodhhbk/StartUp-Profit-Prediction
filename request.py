import requests
url = 'http://localhost:57946/predict_api'
r = requests.post(url,json={'State':'New York','R&D Spend':100000, 'Administration':100000, 'Marketing Spend':100000})

print(r.json())