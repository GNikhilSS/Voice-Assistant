import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print("You said: " + voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")


