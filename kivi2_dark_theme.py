from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        screen=MDScreen()
        return screen


DemoApp().run()