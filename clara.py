#!/usr/bin/env python3

import sys
import logging

from ui import UI
from speech import Speech
from kivy.clock import Clock

class Clara():
    def __init__(self):
        #threading.Thread.__init__(self)
        self.speech_thread = Speech(self.ready, self.thinking, self.recognize_success, self.recognize_failed)
        self.speech_thread.start()
        self.ui = UI()
        self.ui.set_version("clara.2018.001")
        self.ui.register_quit_function(self.exit)
        self.ui.register_mic_function(self.toggle_microphone)
        self.ui.run()
    def exit(self):
        sys.exit()
    def set_conversation(self, text):
        self.conversation_state = "conversation"
        self.voice = text
        self.ui.set_conversation(text)
    def set_error_conversation(self, text):
        self.conversation_state = "error"
        self.voice = text
        self.ui.set_conversation(text)        
        Clock.schedule_once(self.clear_error, 2)
    def clear_error(self, dt):
        if self.conversation_state == "error":
            self.ready()
    def initialising(self):
        self.set_conversation("Initialising...")
    def ready(self):
        self.set_conversation("How can I help?")
    def thinking(self):
        self.set_conversation("Thinking...")
    def recognize_success(self, text):
        self.set_conversation("I heard " + text)
    def recognize_failed(self, error):
        self.set_error_conversation("I failed to recognise what you said")
    def toggle_microphone(self):
        pass


    
if __name__ == '__main__':
    clara = Clara()
