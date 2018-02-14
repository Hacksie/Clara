import speech_recognition as speech

rec = speech.Recognizer()

with speech.Microphone() as source:
    rec.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = rec.listen(source)
    
print("Thinking...")    
try:
    print("Google thinks " + rec.recognize_google(audio))
except speech.UnknownValueError:
    print("Unable to understand you")
except speech.RequestError as e:
    print("MS error: {0}".format(e))