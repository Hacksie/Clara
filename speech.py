
import speech_recognition as speech
import threading
import logging

class Speech(threading.Thread):
    def __init__(self, ready_callback, thinking_callback, recognize_success_callback, recognize_failed_callback):
        threading.Thread.__init__(self)
        self.ready_callback = ready_callback
        self.thinking_callback = thinking_callback
        self.recognize_success_callback = recognize_success_callback
        self.recognize_failed_callback = recognize_failed_callback
        self.microphone = speech.Microphone()
        self.recogniser = speech.Recognizer()
    def run(self):
        with self.microphone as source:
            logging.info("Adjusting for ambient")
            self.recogniser.adjust_for_ambient_noise(source)
        self.listen()
        #self.background_thread = rec.listen_in_background(m, self.callback)
        self.ready_callback()
    def listen(self):
        logging.info("Listening")
        self.background_thread = self.recogniser.listen_in_background(self.microphone, self.callback)
    def callback(self, recognizer, audio):
        self.thinking_callback()
        try:
            spoken = recognizer.recognize_google(audio)
            logging.info("Google recognised " + spoken)
            self.recognize_success_callback(spoken)
        except speech.UnknownValueError:
            logging.warning("Google speech couldn't recognise the audio")
            self.recognize_failed_callback("Google speech couldn't recognise the audio")
        except speech.RequestError:
            logging.warning("Failed to call Google Speech Recognition")
            self.recognize_failed_callback("Failed to call Google Speech Recognition")          
