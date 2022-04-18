from kivymd.app import  MDApp
from kivy.lang import Builder


string_helper="""

Screen:
    MDToolbar:
        pos_hint:{"top":1}
        title:"tool bar title"
        elevation:10
    MDRaisedButton:
        text:"raised button"
        pos_hint:{"center_x":.5,"center_y":.5}
        on_release:app.button_released()



"""

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(string_helper)
        return screen
    def button_released(self):
        print(self)



DemoApp().run()

