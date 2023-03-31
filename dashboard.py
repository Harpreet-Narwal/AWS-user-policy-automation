from tkinter import *
from PIL import Image,ImageTk

class face:
    def __init__(self,window):
        self.window = window
        self.window.title("AWS User Automation App")
        self.window.geometry('1200x675+0+0')

        Boardframe = LabelFrame(self.window,bd=20,bg="black",text ="AWS-IAM User Recommendation System",foreground="white",relief=FLAT,font=('calibri',33))
        Boardframe.place(x=120,y=80,width=900,height=80)
        text_b = Text(Boardframe,width=800, height=595, font=('calibri',12),blockcursor=True,relief=FLAT)
        text_b.pack()

        b1 = Button(window, text = 'User Information',bg='papaya whip',cursor='hand2' ,relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda : user('u')).place(x=450, y= 270)#add,display and edit
        b2 = Button(window, text = 'Roles & Policies', bg='peach puff',cursor='hand2',relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda: rnp('r')).place(x=450, y= 370)#add and dislay

window = Tk()

img=Image.open('images/amazon.jpg')
img=img.resize((1200,675),Image.Resampling.LANCZOS)
photobg=ImageTk.PhotoImage(img)
img_l=Label(window,image=photobg).place(x=0,y=0)

player = face(window)
window.mainloop()