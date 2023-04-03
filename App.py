from tkinter import *
from PIL import Image,ImageTk

class face:
    def __init__(self,window):
        self.window = window
        self.window.title("AWS User Automation App")
        self.window.geometry('1200x675+0+0')

        def u(name):
            if(name=="d"):
                section = Toplevel()
                section.title('All Users')
                section.geometry('1200x675+0+0')

                img=Image.open('images/amazon.jpg')
                img=img.resize((1200,675),Image.Resampling.LANCZOS)
                self.photobg=ImageTk.PhotoImage(img)
                b = Label(section, image=self.photobg)
                b.place(x=0,y=0)

            if(name=="a"):
                section = Toplevel()
                section.title('Add User Details')
                section.geometry('1200x675+0+0')

                img=Image.open('images/amazon.jpg')
                img=img.resize((1200,675),Image.Resampling.LANCZOS)
                self.photobg=ImageTk.PhotoImage(img)
                b = Label(section, image=self.photobg)
                b.place(x=0,y=0)

                w_frame = LabelFrame(section,bd=20,bg="black",relief=FLAT,text ="Fill USER Details ---\n",foreground="white" ,font=('calibri',20))
                w_frame.place(x=120,y=80,width=900,height=600)

                e1=Entry(w_frame,width=76,relief=FLAT,borderwidth=8, font=1)
                e1.insert(0,"Name")
                e1.place(x=7,y=15)
                e2=Entry(w_frame,width=76,relief=FLAT,borderwidth=8, font=1)
                e2.insert(0,"Department 1")
                e2.place(x=7,y=75)
                e3=Entry(w_frame,width=76,relief=FLAT,borderwidth=8, font=1)
                e3.insert(0,"Department 2")
                e3.place(x=7,y=135)

                options = [
                    "Admin",
                    "Product Manganger",
                    "Team Lead",
                    "Employee"
                ]
                clicked = StringVar()
                clicked.set( "Position" )
                drop = OptionMenu( w_frame , clicked , *options)
                drop.config(bg="papaya whip", fg="Black",relief=FLAT)
                drop.place(x=7,y=195,width=300,height=50)
                
                b1 = Button(w_frame, text = 'ADD',bg='green',cursor='hand2' ,relief=FLAT, foreground='black', width=20, height=3,activebackground='light gray', command=lambda : db).place(x=700, y= 195)

            if(name=="md"):
                pass

        def r(name):
            if(name=="d"):
                section = Toplevel()
                section.title('All Policy')
                section.geometry('1200x675+0+0')

                img=Image.open('images/amazon.jpg')
                img=img.resize((1200,675),Image.Resampling.LANCZOS)
                self.photobg=ImageTk.PhotoImage(img)
                b = Label(section, image=self.photobg)
                b.place(x=0,y=0)

            if(name=="ad"):
                pass

        def user():
            section = Toplevel()
            section.title('User Details')
            section.geometry('1200x675+0+0')

            img=Image.open('images/amazon.jpg')
            img=img.resize((1200,675),Image.Resampling.LANCZOS)
            self.photobg=ImageTk.PhotoImage(img)
            b = Label(section, image=self.photobg)
            b.place(x=0,y=0)

            Boardframe = LabelFrame(section,bd=20,bg="black",text ="USER Detail Section",foreground="white",relief=FLAT,font=('calibri',33))
            Boardframe.place(x=120,y=80,width=900,height=80)
            text_b = Text(Boardframe,width=800, height=595, font=('calibri',12),blockcursor=True,relief=FLAT)
            text_b.pack()

            b1 = Button(section, text = 'User Detail Display',bg='papaya whip',cursor='hand2' ,relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda : u("d")).place(x=450, y= 270)
            b2 = Button(section, text = 'Add User', bg='peach puff',cursor='hand2',relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda: u("a")).place(x=450, y= 370)
            b3 = Button(section, text = 'Modify/Delete User', bg='papaya whip',cursor='hand2',relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda: u("md")).place(x=450, y= 470)
            
        def rnp():
            section = Toplevel()
            section.title('Policy Details')
            section.geometry('1200x675+0+0')

            img=Image.open('images/amazon.jpg')
            img=img.resize((1200,675),Image.Resampling.LANCZOS)
            self.photobg=ImageTk.PhotoImage(img)
            b = Label(section, image=self.photobg)
            b.place(x=0,y=0)
            Boardframe = LabelFrame(section,bd=20,bg="black",text ="Policy Detail Section",foreground="white",relief=FLAT,font=('calibri',33))
            Boardframe.place(x=120,y=80,width=900,height=80)
            text_b = Text(Boardframe,width=800, height=595, font=('calibri',12),blockcursor=True,relief=FLAT)
            text_b.pack()

            b1 = Button(section, text = 'Policy Detail Display',bg='papaya whip',cursor='hand2' ,relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda : r("d")).place(x=450, y= 270)
            b2 = Button(section, text = 'Add/Delete Policy', bg='peach puff',cursor='hand2',relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda: r("ad")).place(x=450, y= 370)
    
        Boardframe = LabelFrame(self.window,bd=20,bg="black",text ="AWS-IAM User Recommendation System",foreground="white",relief=FLAT,font=('calibri',33))
        Boardframe.place(x=120,y=80,width=900,height=80)
        text_b = Text(Boardframe,width=800, height=595, font=('calibri',12),blockcursor=True,relief=FLAT)
        text_b.pack()

        b1 = Button(window, text = 'User Information',bg='papaya whip',cursor='hand2' ,relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda : user()).place(x=450, y= 270)#add,display and edit
        b2 = Button(window, text = 'Roles & Policies', bg='peach puff',cursor='hand2',relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda: rnp()).place(x=450, y= 370)#add and dislay

window = Tk()

img=Image.open('images/amazon.jpg')
img=img.resize((1200,675),Image.Resampling.LANCZOS)
photobg=ImageTk.PhotoImage(img)
img_l=Label(window,image=photobg).place(x=0,y=0)

player = face(window)
window.mainloop()