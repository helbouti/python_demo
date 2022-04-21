

from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton


class DemoApp(MDApp):
    def build(self):
        screen = MDScreen()
        
        #username
        self.username=MDTextField()
        self.username.pos_hint={"center_x":.5,"center_y":.5}
        self.username.hint_text="user name"
        self.username.size_hint=(.5,.1)
        #password
        self.password=MDTextField()
        self.password.pos_hint={"center_x":.5,"center_y":.4}
        self.password.hint_text="password"
        self.password.size_hint=(.5,.1)

        #submit button
        self.submit=MDFlatButton(text="Submit")
        #submit.pos=(500,500) use pos_hint instead
        self.submit.pos_hint={"center_x":.5,"center_y":.3}

        #on click event
        self.submit.on_release=lambda : self.clicked()

        #add to screen
        screen.add_widget(self.username)    
        screen.add_widget(self.password)  
        screen.add_widget(self.submit)  
        return screen
        
    def clicked(self):
        print(self.username.text)
        print(self.password.text)



DemoApp().run()