

from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen


class DemoApp(MDApp):
    def build(self):
        screen = MDScreen()
        text_field=MDTextField()
        text_field.pos_hint={"center_x":.5,"center_y":.5}
        #tow new property hint_text and size_hint
        text_field.hint_text="user name"
        text_field.size_hint=(.5,.1)
        screen.add_widget(text_field)    
        return screen


DemoApp().run()