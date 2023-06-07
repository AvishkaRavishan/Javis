import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            print("Request error:", str(e))
        return ""

def text_to_speech(response):
    engine.say(response)
    engine.runAndWait()

# Example usage
while True:
    # Capture user input
    user_input = speech_to_text()

    # Send user input to the GPT-3.5 API and retrieve response
    # Replace the following line with your actual API call code
    response = "This is the response from the GPT-3.5 API."

    # Convert response to speech and play it back
    text_to_speech(response)
