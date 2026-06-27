import requests

cities = [city.strip() for city in input("Enter cities separated by commas: ").split(",")]

for city in cities:
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    try:
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]
    except KeyError:
        print(f"Could not find {city}, skipping...")
        continue

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    temperature = weather_data["current_weather"]["temperature"]
    windspeed = weather_data["current_weather"]["windspeed"]

    print(f"\nWeather in {city}:")
    print(f"  Temperature: {temperature}°C")
    print(f"  Wind speed:  {windspeed} km/h")