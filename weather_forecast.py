import requests
import json
import argparse

API_KEY = '50ddb858a5b1a91ea0a633e3bdddb7ab'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['main']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Error: Could not retrieve weather data for {city}")

if __name__ == '__main__':
    # how to parse input from the command line
    parser = argparse.ArgumentParser(description='Get weather information')
    parser.add_argument('city', help='City for which weather information is to be retrieved')
    args = parser.parse_args()
    get_weather(args.city)
    
