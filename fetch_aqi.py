import requests
import pandas as pd
from datetime import datetime
import os

TOKEN = "d596cfc7e646544c1cf75ec331614623f75182de"

url = f"https://api.waqi.info/map/bounds/?token={TOKEN}&latlng=28.4,76.8,28.9,77.5"

response = requests.get(url)
data = response.json()

rows = []

for s in data["data"]:
    rows.append({
        "station": s["station"]["name"],
        "latitude": s["lat"],
        "longitude": s["lon"],
        "aqi": s["aqi"],
        "timestamp": datetime.now()
    })

df = pd.DataFrame(rows)

file_name = "aqi_data.csv"

if os.path.exists(file_name):
    old = pd.read_csv(file_name)
    df = pd.concat([old, df])

df.to_csv(file_name, index=False)
