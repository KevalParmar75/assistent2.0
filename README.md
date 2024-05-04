# Voice-Controlled Assistant

This project is a voice-controlled assistant that can perform various tasks like playing music on YouTube, opening websites, telling the time and date, and searching on Google. It uses speech recognition to listen to commands and text-to-speech to respond to the user.

## Features

- **Voice Commands**: Interact with the assistant using natural language voice commands.
- **YouTube Playback**: Play music or videos on YouTube by saying "play" followed by your request.
- **Web Browsing**: Open any website by saying "open website" followed by the website name.
- **Time and Date**: Ask for the current time or date.
- **Google Search**: Perform Google searches using voice commands.
- **Customizable Responses**: Modify the assistant's voice and responses.
- **GEMINI AI**: For answering any queries using Google's Gemini ai. 

## Installation

To run this assistant, you need to install the following Python libraries:

```bash
pip install
speech_recognition
pywhatkit
pyttsx3
webbrowser
datetime
google-generativeai


Configuration
Before running the script, make sure to insert your API key in the genai.configure(api_key="your api key") line.

Usage
Run the script using Python

Once the script is running, you can start interacting with the assistant using the following voice commands:
“play [song or video]” to play content on YouTube.
“open website [website name]” to open a website.
“time” to get the current time.
“date” to get the current date.
“gemini [query]” to interact with the Gemini model for generative AI tasks.
“stop” to terminate the program.

Customization
You can customize the assistant’s voice by changing the voices property in the speech function.

Feel free to adjust the content to better fit your project's description and requirements.
