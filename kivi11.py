from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner


class DemoApp(App):
    def build(self):
        screen=Screen()
        menu=Spinner(
            text="Home",
            size_hint=(.2, .08),
            pos_hint= {'top':1},
            values=('Home', 'Work', 'Other', 'Custom')
        )
        sub_menu=Spinner(
            text="ok",
            size_hint=(.2, .08),
            pos_hint= {'center_x':0.3,'top':1},
            values=('Home', 'Work', 'Other', 'Custom')
        )






        screen.add_widget(menu)
        screen.add_widget(sub_menu)
        return screen


DemoApp().run()