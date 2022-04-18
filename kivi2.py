from kivymd.app import MDApp
from kivy.lang import Builder

string_helper="""
Screen:


    
       
"""
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        screen=Builder.load_string(string_helper)
        return screen


DemoApp().run()