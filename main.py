import requests
import keyboard
api_key = "243a9cf392e3d51f429e629236d97f44"


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Извлечение данных о погоде
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]

        # Вывод информации о погоде
        print(f"Погода в городе {city}:")
        print(f"Температура: {temperature}°C")
        print(f"Ощущается как: {feels_like}°C")
        print(f"Влажность: {humidity}%")
        print(f"Скорость ветра: {wind_speed} м/с")
        print(f"Описание: {description}")

        # Дополнительные аспекты погоды
        clouds = weather_data["clouds"]["all"]
        pressure = weather_data["main"]["pressure"]
        visibility = weather_data["visibility"]
        sunrise = weather_data["sys"]["sunrise"]
        sunset = weather_data["sys"]["sunset"]

        print(f"Облачность: {clouds}%")
        print(f"Давление: {pressure} гПа")
        print(f"Видимость: {visibility} м")
        print(f"Время восхода солнца: {sunrise}")
        print(f"Время заката солнца: {sunset}")

        # Прогноз погоды на ближайшие 5 дней
        forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
        forecast_params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }
        forecast_response = requests.get(forecast_url, params=forecast_params)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        print("Прогноз погоды на ближайшие 5 дней:")
        for forecast in forecast_data["list"]:
            date = forecast["dt_txt"]
            forecast_temp = forecast["main"]["temp"]
            forecast_desc = forecast["weather"][0]["description"]
            print(f"Дата: {date}")
            print(f"Температура: {forecast_temp}°C")
            print(f"Описание: {forecast_desc}")
            print("---")

    except requests.exceptions.RequestException as e:
        print("Произошла ошибка при запросе данных о погоде.")
        print(f"Ошибка: {e}")


def main():
    city = input("Введите название города: ")
    get_weather(city)


if __name__ == "__main__":
    main()
print("Нажмите Esc чтобы закрыть программу")
keyboard.wait("Esc")