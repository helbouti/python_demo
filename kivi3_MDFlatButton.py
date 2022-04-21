from cgitb import text
from logging import root
from kivymd.app import  MDApp
from kivymd.uix.button import MDFlatButton



class DemoApp(MDApp):
    def build(self):
        button=MDFlatButton(text="first button")
        button.pos=(500,500)
        return button
    
        



DemoApp().run()

