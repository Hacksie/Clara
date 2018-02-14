

import kivy
kivy.require('1.9.0')
#from kivy.config import Config
#Config.set('graphics', 'fullscreen', '0')
#Config.write()


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

class Container(GridLayout):
    pass

class UI(App):
    # Fix this hack
    def register_quit_function(self, quit_function):
        self.quit_function = quit_function
    def register_mic_function(self, mic_function):
        self.mic_function = mic_function        
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.register_font()
        #LabelBase.register(name="Lato", fn_regular="fonts/Lato-Light.ttf")
        self.container = Container()
        return self.container
    def set_conversation(self, text):
        self.container.conversation_text.text = "[color=000000]"+text+"[/color]"
    def quit_button_pressed(self, *args):
        self.quit_function()
    def mic_button_pressed(self, *args):
        self.mic_function()
    def register_font(self):
        LabelBase.register(name="Cabin", fn_regular="fonts/Cabin-Regular.ttf")
    
