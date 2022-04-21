from distutils.command.build import build
from turtle import screensize
from kivymd.app import MDApp
from kivy.lang import Builder


helper="""

Screen:
    MDToolbar:
        title:"Djanoubcc"
        pos_hint:{"top":1}
        elvation:10    
    BoxLayout:
        orientation:"vertical"
        spacing:5
        padding:5
        size_hint:0.7,0.3
        pos_hint:{"center_x":.5,"center_y":.5}

            
            
        MDTextField:
            size_hint:0.6,0.3
            pos_hint:{"center_x":.5}
            text_hint:"user"

        MDRaisedButton:
            text:"submit"
            size_hint:0.6,0.3
            pos_hint:{"center_x":.5}
            
            
        MDRaisedButton:
            text:"ok kivi is cool"
            size_hint:0.6,0.3
            pos_hint:{"center_x":.5}




"""


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(helper)
        return screen


DemoApp().run()