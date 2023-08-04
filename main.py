#Name:Xing Wu
Date:20230727
import json, requests

def get_weather_data(location):
    # API key from openweathermap.org
    api_key = "7543d8e97eec197add716f5121fe899d"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    try:
        # Determine if the user input is a zip code or a city name
        if location.isdigit():
            params = {"zip": location, "appid": api_key}
        else:
            params = {"q": location, "appid": api_key}

        # Make the API request
        response = requests.get(base_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print("Error: Unable to retrieve weather data. Please try again later.")
            return None

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the weather service. Please check your internet connection.")
        return None

def display_weather_info(weather_data):
    if weather_data is None:
        return

    city_name = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"].capitalize()
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    
    print(f"\nWeather forecast for {city_name}:")
    print(f"Description: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def main():
    print("Welcome to Xing WU Weather Forecast App!")
    
    while True:
        location = input("\nEnter your city or zip code (or 'exit' to quit): ").strip().lower()

        if location == "exit":
            break

        weather_data = get_weather_data(location)
        display_weather_info(weather_data)

if __name__ == "__main__":
    main()
