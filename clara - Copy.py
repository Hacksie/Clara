#!/usr/bin/env python3

#import os
#os.environ['KIVY_WINDOW'] = 'sdl2'

import kivy
kivy.require('1.9.0')
#from kivy.config import Config
#Config.set('graphics', 'fullscreen', '0')
#Config.write()

import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.text import LabelBase
import speech_recognition as speech


import threading
import time

Window.clearcolor = (1, 1, 1, 1)

rec = speech.Recognizer()

class Speech(threading.Thread):
    def __init__(self, ready_callback, thinking_callback, input_callback):
        threading.Thread.__init__(self)
        self.ready_callback = ready_callback
        self.thinking_callback = thinking_callback
        self.input_callback = input_callback
    def run(self):
        print("Starting {}".format(self.name))
        m = speech.Microphone()
        with m as source:
            rec.adjust_for_ambient_noise(source)
        rec.listen_in_background(m, self.callback)
        self.ready_callback()
    def callback(self, recognizer, audio):
        self.thinking_callback()
        #ClaraApp.update(ClaraApp, "test")
        try:
            spoken = recognizer.recognize_google(audio)
            print("I heard " + spoken)
            self.input_callback("I heard:" + spoken)
        except speech.UnknownValueError:
            print("Google speech couldn't recognise the audio")
        except speech.RequestError as e:
            print("Failed to call Google Speech Recognition")          



class Container(GridLayout):
    pass

class Clara(App):
    def build(self):
        self.register_font()
        #LabelBase.register(name="Lato", fn_regular="fonts/Lato-Light.ttf")
        self.container = Container()
        return self.container

    def ready(self):
        self.container.speech_text.text = "[color=000000]Waiting...[/color]"
    def thinking(self):
        self.container.speech_text.text = "[color=000000]Thinking...[/color]"

    def update(self, text):
        print("Update {}".format(text))
        #lblText = ObjectProperty()
        self.container.speech_text.text = "[color=000000]"+text+"[/color]"
    def quit(self, *args):
        print("Quit")
        sys.exit()
    def register_font(self):
        LabelBase.register(name="Cabin", fn_regular="fonts/Cabin-Regular.ttf")
    
if __name__ == '__main__':
    ui = Clara()
    thread1 = Speech(ui.ready, ui.thinking, ui.update)
    thread1.start()
    ui.run()
    #app.run()    
    #while True: time.sleep(0.1)

