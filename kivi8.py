from kivymd.app import MDApp
from kivy.lang import Builder


helper="""
ScreenManager:
    
    First_screen:

    Second_screen:
 

<Second_screen>:
    name:"second_screen"
    MDLabel:
        text:"this is second"
        pos_hint:{"center_y":.5}
    MDFlatButton:
        text:"go to first"
        pos_hint:{"center_y":.7}

<First_screen>:
        name:"first_screen"
        MDLabel:
            text:"this is first"
            pos_hint:{"center_y":.5}

        MDFlatButton:
            text:"go to next"
            pos_hint:{"center_y":.7}
        
"""

class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(helper)

DemoApp().run()