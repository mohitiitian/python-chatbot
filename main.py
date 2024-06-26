import pyttsx3
import speech_recognition as sr
import os
import webbrowser
from config import apikey
import google.generativeai as genai
import emoji



def chat(query):
    genai.configure(api_key=apikey)

    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(history=[])


    response = chat_session.send_message(f"{query}")
    print(f"AI: {response.text}")
    answer = emoji.demojize(response.text)
    say(answer)












def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold= 1
        audio = r.listen(source)
        try:
           querry =r.recognize_google(audio, language="en-in")
           print(f"User said: {querry}")
           return querry
        except Exception as e:
            return "Some Error Occured"
if __name__ == '__main__':
    print('YOYO')
    say("hello I am your assistant")
    while True:
        print("Listening...")
        querry =take_command()
        if querry.lower() == "stop":
            say("Thank you sir")
            break
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in querry.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])
        if querry.lower() == "start chat":
            while True:
                say("Hello How can I help you today")
                print("Listening....")

                query = take_command()
                chat(query)
                if query.lower() == "stop":
                    say("thankyou for chatting")
                    break


