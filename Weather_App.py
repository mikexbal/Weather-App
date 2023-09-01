import requests

#PROMPTS USER FOR CITY
city = input("Enter a city: ")

#GRABS THE LAT/LNG FOR THE USER
latLng = requests.get(f"https://www.mapquestapi.com/geocoding/v1/address?key=78MT1FKjeNjpvquABTg5OM8CiZ1BbGl0&location={city}")
latLng_json = latLng.json()
lat = latLng_json["results"][0]["locations"][0]["latLng"]["lat"]
lng = latLng_json["results"][0]["locations"][0]["latLng"]["lng"]
latLng_json = latLng.json()

#GRABS THE WEATHER
weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}0&appid=1a422019ad78ed7c1e4ab784357ad8da&units=imperial")
weather_json = weather.json()
temp = weather_json["main"]["temp"]
temp_min = weather_json["main"]["temp_min"]
temp_max = weather_json["main"]["temp_max"]
feels_like = weather_json["main"]["feels_like"]

#PRINTS RESULTS
print(f"In {city.upper()} the current temperature is {temp}°F")
print(f"Feels like: {feels_like}°F")
print(f"Toady's High: {temp_max}°F")
print(f"Today's Low: {temp_min}°F")
                

