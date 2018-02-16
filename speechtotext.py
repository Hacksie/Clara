
import speech_recognition as speech
import threading
import logging

class SpeechToText(threading.Thread):
    def __init__(self, config, ready_callback, thinking_callback, recognize_success_callback, recognize_failed_callback):
        threading.Thread.__init__(self)
        self.config = config
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
            if self.config['SpeechToText']['Engine'] == 'wit.ai':
                spoken = recognizer.recognize_wit(audio, key=self.config['SpeechToText']['Key'])
                logging.info("Wit.ai recognised " + spoken)
                self.recognize_success_callback(spoken)
        except speech.UnknownValueError:
            logging.warning("Wit.ai couldn't recognise the audio")
            self.recognize_failed_callback("Clara couldn't recognise the audio")
        except speech.RequestError:
            logging.warning("Failed to call wit.ai recognition")
            self.recognize_failed_callback("Failed to call speech recognition engine")  
