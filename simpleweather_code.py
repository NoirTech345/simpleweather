import requests

def translate_weather_text(text):
    translations = {
        "Clear": "Ясно",
        "Partly cloudy": "Местами облачно",
        "Cloudy": "Облачно",
        "Overcast": "Пасмурно",
        "Mist": "Туман",
        "Patchy rain possible": "Возможен дождь",
        "Moderate rain": "Умеренный дождь",
        "Moderate snow": "Умеренный снег",
        "Light drizzle": "Легкая морось",
        "Heavy rain": "Сильный дождь",
        "Heavy snow": "Сильный снег",
        "Fog": "Туман",
        "Sunny": "Солнечно",
        "Rain shower": "Ливень",
        "Light rain": "Небольшой дождь",
        "Light snow": "Небольшой снег",
        "Thundery outbreaks possible": "Возможны грозы",
        "Blizzard": "Метель",
        "Pellets": "Град",
        "Freezing fog": "Изморозь",
        "Patchy light drizzle": "Местами легкая морось",
        "Patchy light rain": "Местами небольшой дождь",
        "Patchy light snow": "Местами небольшой снег",
        "Patchy moderate snow": "Местами умеренный снег",
        "Patchy heavy snow": "Местами сильный снег",
        "Patchy light rain with thunder": "Местами небольшой дождь с грозой",
        "Patchy light snow with thunder": "Местами небольшой снег с грозой",
        "Moderate or heavy rain shower": "Умеренный или сильный ливень",
        "Moderate or heavy snow showers": "Умеренные или сильные снегопады",
        "Moderate or heavy snow with thunder": "Умеренный или сильный снег с грозой",
        "Patchy rain nearby": "Местами небольшой дождь поблизости",
        "Patchy rain ne…":"Местами небольшой дождь по...",
        "Partly": "Местами",
    }
    for english, russian in translations.items():
        text = text.replace(english, russian)
    return text

def get_weather(city=None):
    if city is None:
        try:
            response = requests.get('http://ip-api.com/json/')
            data = response.json()
            city = data['city']
        except Exception:
            city = input("Не удалось автоматически определить ваш город. Пожалуйста, введите название города: ")

    url = f'https://wttr.in/{city}?lang=ru'
    response = requests.get(url)
    if response.status_code == 200:
        weather_info = response.text
        weather_info = '\n'.join(weather_info.split('\n')[:-2])
        weather_info = translate_weather_text(weather_info)
        return weather_info
    else:
        return "Ошибка при получении данных о погоде"

def main():
    print(get_weather())

if __name__ == "__main__":
    main()
