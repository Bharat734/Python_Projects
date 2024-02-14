import requests
import speech_recognition as sr
import pyttsx3

def get_weather(api_key, city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': api_key}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        if 'message' in data:
            return f'Error: {data["message"]}'
        else:
            temperature = data['main']['temp'] - 273.15
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            result = (
                f'Weather in {city_name}:\n'
                f'Temperature: {temperature:.2f} C\n'
                f'Humidity: {humidity}%\n'
                f'Description: {description}'
            )
            return result

    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Say a location:")
        print("Say a Location...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            location = recognizer.recognize_google(audio).capitalize()
            print(f'Location: {location}')
            return location
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError as e:
            return f"Error with the speech recognition service: {e}"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    api_key = '5faae047c821173974a52d74f2b883ad'  # Replace with your actual API key

    if not api_key:
        print("Please provide a valid API key.")
    else:
        location = get_voice_input()

        if location:
            weather_info = get_weather(api_key, location)

            if weather_info.startswith('Error'):
                print(weather_info)
                speak("Sorry, there was an error fetching the weather information.")
            else:
                print(weather_info)
                speak(weather_info)
