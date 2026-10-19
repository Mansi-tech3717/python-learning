
import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()


def speak(text):
    voice = pyttsx3.init("sapi5")
    voice.setProperty("volume", 1.0)
    voice.say(text)
    voice.runAndWait()
    voice.stop()


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

    else:
        print("Command not recognized")
        speak("Command not recognized")


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
