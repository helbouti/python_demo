
from turtle import title
from kivymd.app import  MDApp
from kivy.lang import Builder

    


helper="""

MDFloatLayout:
   
    


            

    MDToolbar:
        pos_hint:{"top":1}
        title:"Djanoub"
        right_action_items:[["facebook",lambda x:print(x)]]
        elevation:10
    
    MDRaisedButton:
        text:"mybutton"
        pos_hint:{"center_x":.5,"y":.5}
        size_hint:(.8,.1)

    MDRaisedButton:
        text:"mySecondButton"
        pos_hint:{"center_x":.5,"y":.6}
        size_hint:(.8,.1)

"""


class DemoApp(MDApp):
    def build(self):
        screen=Builder.load_string(helper)
            
            

        return screen


DemoApp().run()