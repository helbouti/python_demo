from kivymd.app import MDApp

from kivymd.uix.screen import MDScreen


class DemoApp(MDApp):
    def build(self):
        screen = MDScreen()
        return screen


DemoApp().run()