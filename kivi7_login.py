

from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton


class DemoApp(MDApp):
    def build(self):
        screen = MDScreen()
        
        #username
        username=MDTextField()
        username.pos_hint={"center_x":.5,"center_y":.5}
        username.hint_text="user name"
        username.size_hint=(.5,.1)
        #password
        password=MDTextField()
        password.pos_hint={"center_x":.5,"center_y":.4}
        password.hint_text="password"
        password.size_hint=(.5,.1)

        #submit button
        submit=MDFlatButton(text="Submit")
        #submit.pos=(500,500) user pos_hint instead
        submit.pos_hint={"center_x":.5,"center_y":.3}

        #add to screen
        screen.add_widget(username)    
        screen.add_widget(password)  
        screen.add_widget(submit)  
        return screen


DemoApp().run()