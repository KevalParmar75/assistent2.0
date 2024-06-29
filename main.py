import speech_recognition as sr
import pywhatkit
import pyttsx3
import sys
import webbrowser
import datetime
import google.generativeai as genai
from google.generativeai import GenerativeModel

genai.configure(api_key="your api key")
model = GenerativeModel("gemini-pro")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}


def speech(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)



def get_audio():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1.5)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()  # Return the recognized text

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error: {e}")


def process_command(command):
    if "play" in command:
        speech("Playing on YouTube")
        pywhatkit.playonyt(command)
    elif "stop" in command:
        speech("Stopping the program.")
        sys.exit()

    elif "open website" in command:
        # Extract the website URL from the query
        website = command.replace("open website", "").strip()
        # Add the URL prefix if not provided (e.g., "https://")
        if not website.startswith("http"):
            website_url = "https://www." + website + ".com"
        # Open the website in the default web browser
        webbrowser.open(website)
        speech(f"Opening {website} in your web browser.")
        pywhatkit.search(website_url)

    elif "open website .in" in command:  # Check for a specific condition
        website = command.replace("open website .in", "").strip()
        website_url = "https://www." + website + ".in"
        webbrowser.open(website)
        speech(f"Opening {website} in your web browser.")
        pywhatkit.search(website_url)

    elif "time" in command:
        strfTime = datetime.datetime.now().strftime("%H:%M")
        speech(f"sir time is {strfTime}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speech(f"Current date: {current_date}")

    elif "search" in command:
        speech("Searching on Google")
        pywhatkit.search(command)

    else: # Trigger for Gemini interaction
        prompt = command.replace("gemini", "").strip()  # Extract user query
        response = model.generate_content(contents=prompt)  # Generate response with Gemini
        speech(response.text)  # Speak the generated response


while True:
    command = get_audio()

    if "optimus" in command:
        speech("Optimus here... how may I help you, sir?")
        further_command = get_audio()  # Get further command after "optimus" trigger

        if further_command:
            process_command(further_command)
        else:
            speech("I didn't catch that. Please repeat.")
