from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.uix.popup import Popup


helper="""
MDScreen:
    MDToolbar:
        pos_hint:{"top":1}
        title:"Djanoub"
        right_action_items:[["menu",lambda x:print(x)]]
        

    MDTextField:
        id:user
        hint_text:"User Name"
        pos_hint:{"center_x":.5,"center_y":.7}
        size_hint:(0.6,0.1)

    MDTextField:
        id:password
        hint_text:"Password"
        pos_hint:{"center_x":.5,"center_y":.5}
        password:True
        size_hint:(0.6,0.1)

    MDRaisedButton:
        text:"Submit"
        pos_hint:{"center_x":.5,"center_y":.3}
        size_hint:(.5,0.1)
        on_release:app.clikced()
"""

class DemopApp(MDApp):
    def build(self):
        screen=Builder.load_string(helper)
        return screen
    def clikced(self):
        user=self.root.ids.user.text
        password=self.root.ids.password.text
        if user==password:
            print(self.root.ids.user.text)
            pop=Popup(title="cool",size_hint=(.5,.5))
            pop.open()



DemopApp().run()

