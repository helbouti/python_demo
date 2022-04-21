from tkinter import Button
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton


class DemoApp(MDApp):
    def build(self):
        screen=MDScreen()
        button=MDFlatButton(text="hello python world")
        button.pos=(0,200)
        screen.add_widget(button)
        return screen


DemoApp().run()