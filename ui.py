

import kivy
kivy.require('1.9.0')
#from kivy.config import Config
#Config.set('graphics', 'fullscreen', '0')
#Config.write()

from kivy.app import App
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivymd.label import MDLabel
from kivymd.button import MDIconButton
from kivymd.theming import ThemeManager

class Container(BoxLayout):
    pass

class UI(App):
    theme_cls = ThemeManager() 
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.register_font()
        LabelBase.register(name="Cabin", fn_regular="fonts/Cabin-Regular.ttf")
        self.container = Container()
        self.container.version_text.text = self.version_text
        return self.container
    # FIXME: find a better to register these
    def set_version(self, version_text):
        self.version_text = version_text
    def register_quit_function(self, quit_function):
        self.quit_function = quit_function
    def register_mic_function(self, mic_function):
        self.mic_function = mic_function              
    def set_conversation(self, text):
        self.container.conversation_text.text = text
    def set_input(self, text):
        self.container.input_text.text = text    
    def set_thinking(self, flag):
        pass
        #self.container.spinner.active = flag
        #self.container.input_text.text = text    
    def quit_button_pressed(self, *args):
        self.quit_function()
    def mic_button_pressed(self, *args):
        self.mic_function()
    def register_font(self):
        LabelBase.register(name="Cabin", fn_regular="fonts/Cabin-Regular.ttf")
    
