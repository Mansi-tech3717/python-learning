import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
recognizer = sr.Recognizer()

def speak(text):
    voice = pyttsx3.init("sapi5")
    voice.setProperty("volume", 1.0)
    voice.say(text)
    voice.runAndWait()
    voice.stop()


def chatWithAI(command):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Google Assistant and Alexa."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )
    return completion.choices[0].message.content


def processCommand(command):
    command = command.lower().strip()
    print("Command received:", repr(command))

    if "google" in command:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Opening Google")

    elif "facebook" in command:
        webbrowser.open_new_tab("https://www.facebook.com")
        speak("Opening Facebook")

    elif "youtube" in command:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("Opening YouTube")

    elif "linkedin" in command:
        webbrowser.open_new_tab("https://www.linkedin.com")
        speak("Opening LinkedIn")

    elif command.startswith("play "):
        song = command[5:].strip().lower()

        song_library = {
            name.lower(): link
            for name, link in musicLibrary.music.items()
        }

        if song in song_library:
            webbrowser.open_new_tab(song_library[song])
            speak("Playing " + song)
        else:
            speak("Song not found in music library")
            print("Song not found:", song)

    else:
        try:
            response = chatWithAI(command)
            print("Jarvis:", response)
            speak(response)
        except Exception as e:
            print("OpenAI API error:", e)
            speak("Sorry, something went wrong")


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for Jarvis...")
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Ya")

                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=7
                    )

                command = recognizer.recognize_google(audio)
                processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out. Try again.")

        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")

        except sr.RequestError as e:
            print("Speech recognition error:", e)

        except OSError as e:
            print("Microphone error:", e)
            break