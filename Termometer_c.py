from tkinter import *

class Termometer:
    def __init__(self ,root, name="Termometer",color="bisque"):
        self.root = root
        self.a = 150
        self.main_frame = LabelFrame(root,text=name , bg=color , width=200,height=200)
        self.temp_line = Frame(self.main_frame, bg='grey', width=7,height=100)
        self.temp_line_dakheli = Label(self.main_frame, bg='red',height=100)
        self.myspin = Spinbox(self.main_frame , from_=0,to=100,width=5 ,font=('sans-serif', 11),state="readonly", command=lambda:self.Tchange(color=color))
        self.Label1 = Label(self.main_frame ,width=2,height=1 ,text=100 , bg=color)
        self.Label2 = Label(self.main_frame ,width=2 ,height=1,text=75, bg=color)
        self.Label3 = Label(self.main_frame ,width=2 ,height=1,text=50, bg=color)
        self.Label4 = Label(self.main_frame ,width=2 ,height=1,text=25, bg=color)        
    def Tchange(self,color):
        cordi = int(self.myspin.get())
        cordi -= self.a
        cordi = abs(cordi)
        self.temp_line_dakheli.place(x=95, y=cordi)
        Label(self.main_frame , bg=color,width=7 , height=10).place(x=95,y=171)
    def myplace(self):
        self.main_frame.pack()
        self.temp_line.place(x=95,y=49)
        self.myspin.place(x=70,y=150)
        self.Label1.place(x=105,y=40)
        self.Label2.place(x=74,y=69)
        self.Label3.place(x=105,y=89)
        self.Label4.place(x=74,y=115)

if __name__ == "__main__":
    root = Tk()
    root.geometry('200x200')
    f1 = Termometer(root , "test" , "pink")
    f1.myplace()
    mainloop()