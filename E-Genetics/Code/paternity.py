
from multiprocessing.sharedctypes import Value
from os import chmod
from re import L
from turtle import color
import pandas as pd
from paternityClass import paternityTest
from tkinter import Canvas, Tk, Label, Button, Text, END, Toplevel 
from PIL import ImageTk
from PIL import Image  
from tkinter.filedialog import askopenfile 

     
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.csv')]) 
    if file is not None: 
        data = pd.read_csv(file.name)
        obj = paternityTest()
        
        rsSimilar = obj.check(data['father'], data['mother'], data['child1'], data['combine'])[0]
        rsFather =  obj.check(data['father'], data['mother'], data['child1'], data['combine'])[4]
        rsMother =  obj.check(data['father'], data['mother'], data['child1'], data['combine'])[5]

        rsSimilar = list(dict.fromkeys(rsSimilar))
        rsFather = list(dict.fromkeys(rsFather))
        rsMother = list(dict.fromkeys(rsMother))

        fatherSimilar = obj.check(data['father'], data['mother'], data['child1'], data['combine'])[1]
        motherSimilar = obj.check(data['father'], data['mother'], data['child1'], data['combine'])[2]
        childSimilar = obj.check(data['father'], data['mother'], data['child1'], data['combine'])[3]

        father = obj.check(data['father'], data['mother'], data['child1'], data['combine'])[6]
        mother = obj.check(data['father'], data['mother'], data['child1'], data['combine'])[7]
        chFather = obj.check(data['father'], data['mother'], data['child1'], data['combine'])[8]
        chMother = obj.check(data['father'], data['mother'], data['child1'], data['combine'])[9]
    
        sumSimilar = len(rsSimilar)
        total = (len(rsSimilar)+ len(rsFather))
        sumNotSimilar = len(rsFather)
        rule = sumSimilar / total
        ruleNotSimilar = sumNotSimilar / total
         
        viewScreen = Toplevel(root)
        viewScreen.title("Results")
        viewScreen.geometry("645x400")

        T = Text(viewScreen, height=25, width=80, bg='black', fg='white')
        T.place(x= 0, y=0)
        T.insert(END, "The Number of rsNumbers: {}".format(len(rsSimilar)+ len(rsFather)+len(rsMother)))
        T.insert(END, "\n----------------------------------------")
        T.insert(END, "\nThe Number of rsNumbers fit the rule: {}".format(len(rsSimilar)))
        T.insert(END, "\nRs Numbers: {}".format(rsSimilar[0:5]))
        T.insert(END, "\nFather: {}".format(fatherSimilar[0:5]))
        T.insert(END, "\nChild: {}".format(childSimilar[0:5]))
        T.insert(END, "\nMother: {}".format(motherSimilar[0:5]))
        
        T.insert(END, "\n----------------------------------------")
        T.insert(END, "\nThe Number of rsNumbers does not fit the rule child with father: {}".format(len(rsFather)))
        T.insert(END, "\nDf rsNumber: {}".format(rsFather[0:5]))
        T.insert(END, "\nDf Father: {}".format(father[0:5]))
        T.insert(END, "\nDf Child: {}".format(chFather[0:5]))
       
        T.insert(END, "\n----------------------------------------")
        T.insert(END, "\nThe Number of rsNumbers does not fit the rule child with mother: {}".format(len(rsMother)))
        T.insert(END, "\nDf rsNumber: {}".format(rsMother[0:5]))
        T.insert(END, "\nDf Mother: {}".format(mother[0:5]))
        T.insert(END, "\nDf Child: {}".format(chMother[0:5]))
        T.insert(END, "\n----------------------------------------")
        T.insert(END, "\nSo, The Probability this may be the Fathe: {}".format(rule * 100))
        T.insert(END, "\nSo, The Probability this may Not be the Father: {}".format(ruleNotSimilar * 100))
       
        T.config(state='disabled')
        
        print('The Number of rsNumbers', len(rsSimilar)+ len(rsFather)+len(rsMother)-4)
        print('\n\nThe Number of rsNumbers fit the rule', len(rsSimilar))
        print('The Similar rsNumber', rsSimilar[0:5])  
        print('Father: ', fatherSimilar[0:5])
        print('Child', childSimilar[0:5])
        print('Mother', motherSimilar[0:5])
        print('\n\nDifference between Father and Child')
        print('The Number of rsNumbers does not fit the rule child with father', len(rsFather))
        print('Df rsNumber', rsFather[0:5])
        print('Df Father', father[0:5])
        print('Df Child', chFather[0:5])
        print('\n\nDifference between Mother and Child')
        print('The Number of rsNumbers does not fit the rule child with mother', len(rsMother))
        print('Df rsNumber', rsMother[0:5])
        print('Df Child', chMother[0:5])
        print('Df Mother', mother[0:5])
        print("So, The Probability this may be the Father: ", rule * 100)
        print("So, The Probability this may Not be the Father: ", ruleNotSimilar * 100)
      
if __name__ == "__main__":
  root = Tk()  
  root.title('paternityTest')
  canvas = Canvas(root, width = 500, height = 500)  
  canvas.pack()
  load = Image.open("family-law.png")
  render = ImageTk.PhotoImage(load) 
  img = Label(image=render)
  img.image = render
  img.place(x=0, y=0)
  btn = Button(root, text= 'Browse',  command= lambda:open_file(), background='black',fg='white')
  
  btn.place(x= 200, y=450)
  root.mainloop()  
  



    