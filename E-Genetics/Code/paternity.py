
from os import chmod
from re import L
from turtle import color
import pandas as pd
from paternityClass import paternityTest
from tkinter import Canvas, Tk, Label, Button, Entry, END 
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

        Label(root, text= ('The Number of rsNumbers')).place(x= 400, y=0)
        Label(root, text= (len(rsSimilar)+ len(rsFather)+len(rsMother)-4), fg='Red').place(x= 450, y=25)   
        print('The Number of rsNumbers', len(rsSimilar)+ len(rsFather)+len(rsMother)-4)
       
        Label(root, text= ('The Number of rsNumbers fit the rule')).place(x= 400, y=50)
        Label(root, text= (len(rsSimilar)), fg='Red').place(x= 450, y=75)
        print('\n\nThe Number of rsNumbers fit the rule', len(rsSimilar))
       
        Label(root, text= ('The Similar rsNumber')).place(x= 400, y=100)
        Label(root, text= (rsSimilar[0:5]), fg='Red').place(x= 450, y=125)
        print('The Similar rsNumber', rsSimilar[0:5])  
       
        Label(root, text= ('Father')).place(x= 400, y=150)
        Label(root, text= (fatherSimilar[0:5]), fg='Red').place(x= 450, y=175)
        print('Father', fatherSimilar[0:5])
       
        Label(root, text= ('Child')).place(x= 400, y=200)
        Label(root, text= (childSimilar[0:5]), fg='Red').place(x= 450, y=225)
        print('Child', childSimilar[0:5])
       
        Label(root, text= ('Mother')).place(x= 400, y=250)
        Label(root, text= (motherSimilar[0:5]), fg='Red').place(x= 450, y=275)
        print('Mother', motherSimilar[0:5])
      
        Label(root, text= 'Difference between Father and Child').place(x= 400, y=300)
        print('\n\nDifference between Father and Child')
       
        Label(root, text= ('The Number of rsNumbers does not fit the rule child with father')).place(x= 400, y=325)
        Label(root, text= (len(rsFather)), fg='Red').place(x= 450, y=350)
        print('The Number of rsNumbers does not fit the rule child with father', len(rsFather))

        Label(root, text= ('Df rsNumber')).place(x= 400, y=375)
        Label(root, text= (rsFather[0:5]), fg='Red').place(x= 450, y=400)
        print('Df rsNumber', rsFather[0:5])
       
        Label(root, text= ('Df Father')).place(x= 400, y=425)
        Label(root, text= (father[0:5]), fg='Red').place(x= 450, y=450)
        print('Df Father', father[0:5])
       
        Label(root, text= ('Df Child')).place(x= 400, y=475)
        Label(root, text= (chFather[0:5]), fg='Red').place(x= 450, y=500)
        print('Df Child', chFather[0:5])
       
        Label(root, text= 'Difference between Mother and Child').place(x= 400, y=525)
        print('\n\nDifference between Mother and Child')

        Label(root, text= ('The Number of rsNumbers does not fit the rule child with mother')).place(x= 400, y=550)
        Label(root, text= (len(rsMother)), fg='Red').place(x= 450, y=575)
        print('The Number of rsNumbers does not fit the rule child with mother', len(rsMother))
       
        Label(root, text= ('Df rsNumber')).place(x= 400, y=600)
        Label(root, text= (rsMother[0:5]), fg='Red').place(x= 450, y=625)
        print('Df rsNumber', rsMother[0:5])
       
        Label(root, text= ('Df Child')).place(x= 400, y=650)
        Label(root, text= (chMother[0:5]), fg='Red').place(x= 450, y=675)
        print('Df Child', chMother[0:5])
       
        Label(root, text= ('Df Mother')).place(x= 400, y=700)
        Label(root, text= (mother[0:5]), fg='Red').place(x= 450, y=725)
        print('Df Mother', mother[0:5])

if __name__ == "__main__":
  root = Tk()  
  root.title('paternityTest')
  canvas = Canvas(root, width = 900, height = 800)  
  canvas.pack()
  load = Image.open("street.png")
  render = ImageTk.PhotoImage(load) 
  img = Label(image=render)
  img.image = render
  img.place(x=0, y=0)
  btn = Button(root, text= 'Browse',  command= lambda:open_file())
  
  btn.place(x= 80, y=280)
  root.mainloop()  
  



    