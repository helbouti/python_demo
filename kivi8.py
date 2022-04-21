
#cant fix error in this code iam not ready yeat
from kivymd.app import MDApp
from kivy.lang import Builder



class DemoApp(MDApp):
    def build(self):
        screen =Builder.load_file("kv8.kv")
        return screen

DemoApp().run()