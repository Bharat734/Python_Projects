import speech_recognition as sr
import pyautogui

def take_screenshot():
    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot
    screenshot.save('screenshot.png')

    print('Screenshot taken and saved')

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

        try:
            audio = recognizer.listen(source, timeout=50000)
            command = recognizer.recognize_google(audio).lower()

            if 'screenshot' in command:
                take_screenshot()
            else:
                print("Command not recognized.")

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service; {e}")

if __name__ == "__main__":
    listen_for_command()
