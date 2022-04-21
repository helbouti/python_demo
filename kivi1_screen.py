from turtle import title
from kivymd.app import MDApp

from kivymd.uix.screen import MDScreen
from numpy import tile


class DemoApp(MDApp):
    def build(self):
        screen = MDScreen()
        screen.md_bg_color=(.3,.3,.3,.3)
        return screen


DemoApp().run()