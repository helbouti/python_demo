
from kivymd.app import MDApp
from kivy.lang import Builder


helper="""
Screen:
    MDRaisedButton:
        text:"this is mdbutton"
        pos_hint:{"center_x":.5,"center_y":.5}
        

"""

class DemoApp(MDApp):
    def build(self):
        screen =Builder.load_string(helper)
        return screen

DemoApp().run()