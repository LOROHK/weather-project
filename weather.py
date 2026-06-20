import requests

latitude = -4.0435
longitude = 39.6682

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = requests.get(url)
data = response.json()

print(data)  # <-- add this line temporarily

temperature = data["current_weather"]["temperature"]
print("Current temperature:", temperature)





