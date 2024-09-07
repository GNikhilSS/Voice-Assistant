import Speech_to_text
import Text_to_speech
import weather

import datetime
import webbrowser
import AppOpener as ap

def action(data):
    if data == "":
        Text_to_speech.text_to_speech("Hi ! Tell me what to do")
        return "Hi! Tell me what to do"

    user_data = data.lower()
    if "hello" in user_data:
        Text_to_speech.text_to_speech("Hi Hello Namaste!!")
        return "Hi Hello Namaste!!"
    
    elif "open whatsapp" in user_data:
        ap.open("whatsapp", match_closest=True)
        Text_to_speech.text_to_speech("whatsapp opened")
        return "whatsapp opened"
    
    elif "open calculator" in user_data:
        ap.open("calculator", match_closest=True)
        Text_to_speech.text_to_speech("calculator opened")
        return "calculator opened"

    elif "open camera" in user_data:
        ap.open("camera", match_closest=True)
        Text_to_speech.text_to_speech("camera opened")
        return "camera opened"

    elif "open vscode" in user_data:
        ap.open("visual studio code", match_closest=True)
        Text_to_speech.text_to_speech("vscode opened")
        return "vscode opened"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        Text_to_speech.text_to_speech("youtube opened")
        return "youtube opened"
    
    elif "open gmail" in user_data:
        webbrowser.open("https://accounts.google.com/servicelogin?service=mail")
        Text_to_speech.text_to_speech("gmail opened")
        return "gmail opened"
    
    elif "open amazon" in user_data:
        webbrowser.open("https://www.amazon.in/")
        Text_to_speech.text_to_speech("amazon opened")
        return "amazon opened"

    elif "weather in" in user_data:
        for i in range(len(user_data)):
            if user_data[i] == "weather":
                p = user_data[i+2]
                Text_to_speech.text_to_speech(weather.weather(p))
                return weather.weather(p)        

    elif "time now" in user_data:
        time = datetime.datetime.now()
        time = (str)(time.hour) + " : " + (str)(time.minute)  
        Text_to_speech.text_to_speech(time)
        return time
    
    elif "bye" in user_data:
        Text_to_speech.text_to_speech("Take care")
        return "Take care"

    else:
        Text_to_speech.text_to_speech("Could you Please repeat again. I couldn't quiet get that")
        return "Could you Please repeat again. I couldn't quiet get that"

