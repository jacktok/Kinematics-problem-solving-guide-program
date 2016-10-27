from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
import controller as con
from kivy.uix.label import Label

                        
                

class app(App):
	def build(self):
		return main()

class main(FloatLayout):
       
        def getInput(self):
                self.ids["problem"].text=con.getInput(self.ids["problem"].text)
              
       
        def getChangE(self):
                self.ids["problem"].text=con.getChangE(self.ids["problem"].text)

        def getE(self):
                self.ids["problem"].text=con.getE(self.ids["problem"].text)                
                
       
    
app().run()
