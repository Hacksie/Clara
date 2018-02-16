
import threading
import os

class TextToSpeech(threading.Thread):
    def __init__(self, config, text):
        threading.Thread.__init__(self)
        self.config = config
        self.text = text        
    def run(self):    
        os.system('flite -t "' + self.text + '" -voice slt')