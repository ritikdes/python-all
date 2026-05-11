import requests

KATHMANDU_URL = "https://api.open-meteo.com/v1/forecast?latitude=27.7172&longitude=85.3240&current_weather=true"
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_condition_name(code):
    if code == 0:
        return "Clear Sky"
    elif 1 <= code <= 3:
        return "Partly Cloudy/Overcast"
    elif 45 <= code <= 48:
        return "Foggy"
    elif 51 <= code <= 67:
        return "Drizzle or Rain"
    elif 71 <= code <= 77:
        return "Snowfall"
    elif 80 <= code <= 82:
        return "Rain Showers"
    elif code >= 95:
        return "Thunderstorm"
    else:
        return "Unknown Weather Code"

try:
    response = requests.get(KATHMANDU_URL, timeout=5)
    response.raise_for_status()

    data = response.json()
    weather = data['current_weather']
    condition = get_condition_name(weather['weathercode'])
    print("=======================")
    print("      WEATHER APP")
    print("=======================")
    print("Kathmandu")
    print(f" Temperature: {weather['temperature']} C | Windspeed: {weather['windspeed']} km/h | Condition: {condition}")

except requests.exceptions.RequestException as e:
    print(f"Internet/API Error: {e}")




def get_coordinates(city):
    try:
        response = requests.get(GEOCODING_URL, params={"name": city, "count":1}, timeout=5)
        response.raise_for_status()

        data = response.json()
        if "results" not in data or len(data["results"]) == 0:
            print(f"'{city}' not found")
            return None, None
        result = data["results"][0]
        lat = result['latitude']
        lon = result['longitude']
        return lat, lon
        
    except requests.exceptions.RequestException as e:
        print(f"Internet/API Error: {e}")
    

    
def get_weather(lat, lon):
    try:
        response = requests.get(WEATHER_URL, params={"latitude":lat, "longitude":lon, "current_weather":True}, timeout=5)
        response.raise_for_status()

        data = response.json()
        weather = data['current_weather']
        condition = get_condition_name(weather['weathercode'])
        print(f" Temperature: {weather['temperature']} C | Windspeed: {weather['windspeed']} km/h | Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Internet/API Error: {e}")    


    

print()
city = input("Which city do you want to check?: ")
lat, lon = get_coordinates(city)
if lat is not None and lon is not None:
    get_weather(lat, lon)
