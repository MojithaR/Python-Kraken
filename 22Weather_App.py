# Weather_App.py

import requests

def get_weather(city):
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        return (f"Temperature: {temp}\n"
                f"Pressure: {pressure}\n"
                f"Humidity: {humidity}\n"
                f"Description: {description}")
    else:
        return "City Not Found"

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))
