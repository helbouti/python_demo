from random import Random
from kivymd.app import MDApp
from kivy.animation import Animation
import random


class MainApp(MDApp):
    pass

        
    def dummy_function(self):
        print(self.root.ids.password_field)
       

        
        

        

MainApp().run()


"""
 MDBoxLayout:
#            md_bg_color: 0,0,100/255,1
            orientation: 'vertical'
            md_bg_color:1,0,1,1
            
            MDRaisedButton:
                
                text:"button"
                pos_hint:{"center_y":.5,"center_y":.5}
            Widget:"""
