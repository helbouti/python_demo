from kivymd.app import MDApp

from kivy.lang import Builder
from kivymd.uix.bottomsheet import MDGridBottomSheet,MDListBottomSheet

helper="""
Screen:
    FloatLayout:
        MDRaisedButton:
            text:"open grid"
            pos_hint:{"center_x":0.5,"center_y":0.5}
            on_release:app.grid_release()

        MDRaisedButton:
            text:"open list"
            pos_hint:{"center_x":0.5,"center_y":0.57}
            on_release:app.list_release()

        
         
"""



class DemoApp(MDApp):
    
    def build(self):
        screen=Builder.load_string(helper)
        return screen

    def grid_action(self):
        print("facebook")
       
        

    def grid_release(self):
        print("grid_release")
        bs=MDListBottomSheet()
        bs.add_item(
            text="faceboock",
            callback=lambda x:self.grid_action(),
            icon="facebook"
        )
        bs.open()

    def list_release(self):
        print("list_release")
        bs=MDGridBottomSheet()
        bs.add_item(
            text="faceboock",
            callback=lambda x:self.grid_action(),
            icon_src="facebook"
        )
        bs.open()

DemoApp().run()