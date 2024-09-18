import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

kivy.require("2.3.0")




class Layoutt(BoxLayout):
    global seir
    seir = 0
    

    def __init__(self):
        super(Layoutt,self).__init__()

    def minus(self): 
        if (seir == 1):
            label = self.ids.mainlabel.text
            value = round(float(label) - 0.1 , 2)
            self.ids.mainlabel.text = str(value)
            txt = open("tips" , "w")
            txt.write(str(value))
            txt.close
          
        
        if (seir == 2):
            label = self.ids.mainlabel.text
            value = int(label) - 1
            self.ids.mainlabel.text = str(value)
            txt = open("gas" , "w")
            txt.write(str(value))
            txt.close

        
            
        if (seir == 3):
            label = self.ids.mainlabel.text
            value = int(label) - 5
            self.ids.mainlabel.text = str(value)
            txt = open("bank" , "w")
            txt.write(str(value))
            txt.close

        if (seir == 4):
            label = self.ids.mainlabel.text
            value = int(label) - 5
            self.ids.mainlabel.text = str(value)
            txt = open("supra" , "w")
            txt.write(str(value))
            txt.close

        
    def plus(self):
        if (seir == 1):
            label = self.ids.mainlabel.text
            value = round(float(label) + 0.1 , 2)
            self.ids.mainlabel.text = str(value)
            txt = open("tips" , "w")
            txt.write(str(value))
            txt.close

        if (seir == 2):
            label = self.ids.mainlabel.text
            value = int(label) + 1
            self.ids.mainlabel.text = str(value)
            txt = open("gas" , "w")
            txt.write(str(value))
            txt.close

        if (seir == 3):
            label = self.ids.mainlabel.text
            value = int(label) + 5
            self.ids.mainlabel.text = str(value)
            txt = open("bank" , "w")
            txt.write(str(value))
            txt.close
        
        if (seir == 4):
            label = self.ids.mainlabel.text
            value = int(label) + 5
            self.ids.mainlabel.text = str(value)
            txt = open("supra" , "w")
            txt.write(str(value))
            txt.close
            
       
      
    
    def onTips(self):
        global seir 
        seir = 1
        self.ids.seclabel.text = "Tips €"
        txt = open("tips" , "r")
        self.ids.mainlabel.text = str(txt.read())              
        txt.close
     
        
    
    def onGas(self):
        global seir 
        seir = 2
        self.ids.seclabel.text = "Gas €"
        txt = open("gas" , "r")
        self.ids.mainlabel.text = str(txt.read())              
        txt.close
    

    def onBank(self):
        global seir
        seir = 3
        txt = open("bank" , "r")
        self.ids.mainlabel.text = str(txt.read())
        self.ids.seclabel.text = "€heck"              
        txt.close
      

    def onSupra(self):
        global seir 
        seir = 4
        txt = open("supra" , "r")
        self.ids.mainlabel.text = str(txt.read()) 
        self.ids.seclabel.text = "Pizdets €"             
        txt.close

    
    
       
        

class DeBoy(App):
    def build(self):
        return Layoutt()


x=DeBoy()
x.run()
