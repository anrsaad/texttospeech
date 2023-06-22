import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Example usage
text_to_speech("hello friends, welcome to codenza channel. please be sure to subscribe. thank you")
