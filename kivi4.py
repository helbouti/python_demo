from kivymd.app import MDApp

from kivy.lang import Builder

helper="""

Screen:
    MDBoxLayout:
        orientation:"vertical"
        MDToolbar:
            title:"this is my app"
            pos_hint:{"top":1}
            elevation:10
        MDRaisedButton:
            text:"this is button"
            pos_hint:{"center_x":.5,"center_y":.5}
        MDSlider:
            min:0
            max:10
            value:3
"""

class DemoApp(MDApp):
    def build(self):
        screen=Builder.load_string(helper)
        return screen


DemoApp().run()