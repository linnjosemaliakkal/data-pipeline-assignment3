import requests, json
from datetime import datetime

url = "https://api.alternative.me/fng/"
params = {"limit": 365}

response = requests.get(url, params=params)
data = response.json()

ts = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
filename = f"data/bronze/fear_greed_{ts}.json"

with open(filename, "w") as f:
    json.dump(data, f, indent=2)

print("Saved Fear & Greed data")

