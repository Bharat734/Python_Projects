import requests
import speech_recognition as sr
import pyttsx3
from link import blink

def get_joke():
    url = blink
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'twopart':
            joke = f"{data['setup']} {data['delivery']}"
        else:
            joke = data['joke']
        return joke
    else:
        return "Failed to fetch joke"

def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Say something:")
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text_input = recognizer.recognize_google(audio)
            print(f'You said: {text_input}')
            return text_input
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError as e:
            return f"Error with the speech recognition service: {e}"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    joke_input = get_voice_input()

    if joke_input:
        if 'joke' in joke_input.lower():
            joke = get_joke()
            print(joke)
            speak(joke)
        else:
            print("You didn't ask for a joke.")
            speak("You didn't ask for a joke.")















