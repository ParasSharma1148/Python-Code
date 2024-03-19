import requests

def get_weather(city):
    api_key = "f306bdd37f6825ec076e4472c13cc8c6"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            print(f"Weather in {city}:")
            print(f"Description: {weather_description.capitalize()}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("City not found.")
    
    except Exception as e:
        print("An error occurred:", e)

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
