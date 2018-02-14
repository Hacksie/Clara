#!/usr/bin/env python3

import sys
import logging

from ui import UI
from speech import Speech


class Clara():
    def __init__(self):
        #threading.Thread.__init__(self)
        self.speech_thread = Speech(self.ready, self.thinking, self.recognize_success, self.recognize_failed)
        self.speech_thread.start()
        self.ui = UI()
        self.ui.register_quit_function(self.exit)
        self.ui.register_mic_function(self.toggle_microphone)
        self.ui.run()
    def exit(self):
        sys.exit()
    def initialising(self):
        self.ui.set_conversation("Initialising...")
    def ready(self):
        self.ui.set_conversation("How can I help?")
    def thinking(self):
        self.ui.set_conversation("Thinking...")
    def recognize_success(self, text):
        self.ui.set_conversation("I heard " + text)
    def recognize_failed(self, error):
        self.ui.set_conversation("I failed to recognise what you said")
    def toggle_microphone(self):
        pass


    
if __name__ == '__main__':
    clara = Clara()
