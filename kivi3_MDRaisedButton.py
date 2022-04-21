from cgitb import text
from logging import root
from kivymd.app import  MDApp
from kivymd.uix.button import MDRaisedButton



class DemoApp(MDApp):
    def build(self):
        button=MDRaisedButton(text="first button")
        button.pos=(500,500)
        return button
    
        



DemoApp().run()

