

from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen


class DemoApp(MDApp):
    def build(self):
        screen = MDScreen()


        #user
        text_field=MDTextField()
        text_field.pos_hint={"center_x":.5,"center_y":.5}
        text_field.hint_text="user name"
        text_field.size_hint=(.5,.1)

        
        #password
        password_field=MDTextField()
        password_field.pos_hint={"center_x":.5,"center_y":.6}
        password_field.hint_text="user name"
        password_field.size_hint=(.5,.1)
        password_field.padding=True


        #add to screen
        screen.add_widget(text_field)    
        screen.add_widget(password_field)    
        return screen


DemoApp().run()