# weather_fetcher.py
import requests

def get_weather(city_name, api_key):
    """
    Fetches weather information for a given city.

    Parameters:
    city_name (str): Name of the city to fetch the weather for.
    api_key (str): API key for OpenWeatherMap.

    Returns:
    dict: Weather information for the city.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Get temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather_info(weather_data):
    """
    Displays weather information.

    Parameters:
    weather_data (dict): Weather data to display.
    """
    if weather_data:
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("City not found or there was an error fetching the weather information.")

def main():
    """
    Main function to execute the weather fetching script.
    """
    city_name = input("Enter the city name: ")
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    weather_data = get_weather(city_name, api_key)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
