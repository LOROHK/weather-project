import requests

city_name = input("Enter a city name: ")

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
geo_response = requests.get(geo_url)
geo_data = geo_response.json()

try:
    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]
except KeyError:
    print("Sorry, I couldn't find that city. Try again?")
    exit()

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
weather_response = requests.get(weather_url)
weather_data = weather_response.json()

temperature = weather_data["current_weather"]["temperature"]
windspeed = weather_data["current_weather"]["windspeed"]

print(f"Weather in {city_name}:")
print(f"  Temperature: {temperature}°C")
print(f"  Wind speed: {windspeed} km/h")
