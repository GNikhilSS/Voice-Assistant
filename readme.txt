# Simple Voice Assistant
#### Video Demo:  https://youtu.be/WP7Sky0NqAs?si=jX_AblO0HJYn3QmR
#### Description:
    I have developed a simple voice assistant. My main tech stack is python only.
    Via using python, i have implemented various features like recieving user's commands via voice, giving bot generated responses
    , and also performing few actions which are likely to be used by the user.
    By using this app, user can open certain apps in their pc or go to certain webpages.
    They can also have time, weather and so on.
    Further actions can be developed by simply tinkering the action page.
    
    Speech_to_text.py program consists of a function which allows for the user's voice command to be converted into text and return it.
    It uses SpeechRecognition library and the Recognizer method to grasp the audio. Then it uses methods like listen and recoginze_google
    to convert the speech into voice
    
    Text_to_speech.py program consists of a funciton which allows any text to be converted into speech. With this we replicate the assistant's
    speech. It uses pyttsx3 library which has methods like getProperty and setProperty.

    weather.py program consists of a funciton which allows to find the weather of an area in real time. It uses HTMLSESSION library. The function
    searches weather in so and so city. Then it finds the temperature and weather type values by matching with their class values. Then the weather
    can be obtained

    action.py program consists of all the actions which can be implemented using the app. Here you can add further actions which can be personalised
    From greeting the user to saying bye, you can add whatever u could, which have been already implemented.

    interface.py program consists of all the styling, buttons and other stuff which make the app more like an app. It uses tkinter library. It also
    user PIL library to display any image of ur liking

    In conclusion this simple voice assistant is just a really nice thing to have to automate some of your daily tasks like if you use VS code daily,
     you can simple ask it to open for you. That is all.

    Thank you...
