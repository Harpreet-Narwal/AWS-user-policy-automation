from tkinter import *
from PIL import Image,ImageTk

class face:
    def __init__(self,window):
        self.window = window
        self.window.title("AWS User Automation App")
        self.window.geometry('1200x675+0+0')

        Boardframe = LabelFrame(self.window,bd=20,bg="white",text ="AWS-IAM User Recommendation System",relief=FLAT,font=('calibri',12))
        Boardframe.place(x=120,y=80,width=900,height=80)
        text_b = Text(Boardframe,width=800, height=595, font=('calibri',14),blockcursor=True,relief=FLAT)
        text_b.pack()

window = Tk()

img=Image.open('images/amazon.jpg')
img=img.resize((1200,675),Image.Resampling.LANCZOS)
photobg=ImageTk.PhotoImage(img)
img_l=Label(window,image=photobg).place(x=0,y=0)

player = face(window)
window.mainloop()