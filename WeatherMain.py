# demonstrates basic weather data retrieval and display functionality
import requests
city = "London"
def get_weather_data(city):
    api_key = "09067ec1bbd77a2996d3f4b9810d93f7"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data):
    if not data:
        print("No data available.")
        return
    cod = data.get("cod")
    if cod == 200 or str(cod) == "200":
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        print(f"Temperature: {main.get('temp', 'N/A')}°C")
        print(f"Humidity: {main.get('humidity', 'N/A')}%")
        print(f"Weather Description: {weather.get('description', 'N/A')}")
    else:
        message = data.get("message", "City Not Found")
        print(f"Error: {message}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather_data(city)
    display_weather(weather_data)

# Note: Replace the API key above with your own OpenWeatherMap API key if needed.