from tkinter import *
from PIL import Image,ImageTk
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="",port="3306",databse="")
c=con.cursor()

class face:
    def __init__(self,window):
        self.window = window
        self.window.title("AWS User Automation App")
        self.window.geometry('1200x675+0+0')

        def db(name,d1,d2,position):
            query = "insert into db (colname) values(%s,%s,%s,%s)"
            vals = (name,d1,d2,position)
            c.execute(query,vals)
            con.commit()

            c.execute(f'select policyname from policy where {position}="YES"')
            policy = []
            for i in c:
                policy.append(i[0])

            section = Toplevel()
            section.title(name)
            section.geometry('1200x675+0+0')

            img=Image.open('images/amazon.jpg')
            img=img.resize((1200,675),Image.Resampling.LANCZOS)
            self.photobg=ImageTk.PhotoImage(img)
            b = Label(section, image=self.photobg)
            b.place(x=0,y=0)

            w_frame = LabelFrame(section,bd=20,bg="white",relief=FLAT,text ="USER Details ---\n",foreground="white" ,font=('calibri',20))
            w_frame.place(x=120,y=80,width=900,height=600)

            l1 = Label(w_frame,text=name,font=('calibri',18)).pack()
            l2 = Label(w_frame,text=d1,font=('calibri',18)).pack()
            l3 = Label(w_frame,text=d2,font=('calibri',18)).pack()
            l4 = Label(w_frame,text=position,font=('calibri',18)).pack()

            clicked = StringVar()
            clicked.set( "Recommended Policy" )
            drop = OptionMenu( w_frame , clicked , *policy)
            drop.config(bg="papaya whip", fg="Black",relief=FLAT)
            drop.place(x=7,y=195,width=300,height=50)

            def enter(pol,n):
                c.execute(f'insert into db (colname) values({[pol]}) where name={n}')
                con.commit()

            b1 = Button(w_frame, text = 'ADD',bg='green',cursor='hand2' ,relief=FLAT, foreground='black', width=20, height=3,activebackground='light gray', command=lambda : enter(clicked.get(),name)).place(x=700, y= 195)


        def dbp(name,c1,c2,c3,c4):
            query = "insert into db (colname) values(%s,%s,%s,%s,%s)"
            vals = (name,c1,c2,c3,c4)
            c.execute(query,vals)
            con.commit()

        def u(name):
            if(name=="md"):
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
                    "ProductManganger",
                    "TeamLead",
                    "Employee"
                ]
                clicked = StringVar()
                clicked.set( "Position" )
                drop = OptionMenu( w_frame , clicked , *options)
                drop.config(bg="papaya whip", fg="Black",relief=FLAT)
                drop.place(x=7,y=195,width=300,height=50)
                
                b1 = Button(w_frame, text = 'ADD',bg='green',cursor='hand2' ,relief=FLAT, foreground='black', width=20, height=3,activebackground='light gray', command=lambda : db(e1.get(),e2.get(),e3.get(),clicked.get())).place(x=700, y= 195)

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
                section = Toplevel()
                section.title('Add Policy Details')
                section.geometry('1200x675+0+0')

                img=Image.open('images/amazon.jpg')
                img=img.resize((1200,675),Image.Resampling.LANCZOS)
                self.photobg=ImageTk.PhotoImage(img)
                b = Label(section, image=self.photobg)
                b.place(x=0,y=0)

                w_frame = LabelFrame(section,bd=20,bg="black",relief=FLAT,text ="Fill Policy Details ---\n",foreground="white" ,font=('calibri',20))
                w_frame.place(x=120,y=80,width=900,height=600)

                e1=Entry(w_frame,width=76,relief=FLAT,borderwidth=8, font=1)
                e1.insert(0,"Name")
                e1.place(x=7,y=15)

                options = [
                    "YES",
                    "NO"
                ]
                clicked1 = StringVar()
                clicked1.set( "Admin Access" )
                drop = OptionMenu( w_frame , clicked1 , *options)
                drop.config(bg="papaya whip", fg="Black",relief=FLAT)
                drop.place(x=7,y=75,width=300,height=50)

                clicked2 = StringVar()
                clicked2.set( "Product Manager Access" )
                drop = OptionMenu( w_frame , clicked2 , *options)
                drop.config(bg="papaya whip", fg="Black",relief=FLAT)
                drop.place(x=7,y=135,width=300,height=50)

                clicked3 = StringVar()
                clicked3.set( "Team Lead Access" )
                drop = OptionMenu( w_frame , clicked3 , *options)
                drop.config(bg="papaya whip", fg="Black",relief=FLAT)
                drop.place(x=7,y=195,width=300,height=50)

                clicked4 = StringVar()
                clicked4.set( "Employee Access" )
                drop = OptionMenu( w_frame , clicked4 , *options)
                drop.config(bg="papaya whip", fg="Black",relief=FLAT)
                drop.place(x=7,y=255,width=300,height=50)
                
                b1 = Button(w_frame, text = 'ADD',bg='green',cursor='hand2' ,relief=FLAT, foreground='black', width=20, height=3,activebackground='light gray', command=lambda : dbp(e1.get(),clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get())).place(x=700, y= 255)


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

            b1 = Button(section, text = 'User Detail Display',bg='papaya whip',cursor='hand2' ,relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda : u("md")).place(x=450, y= 270)
            b2 = Button(section, text = 'Add User', bg='peach puff',cursor='hand2',relief=FLAT, foreground='black', width=35, height=4,activebackground='light gray', command=lambda: u("a")).place(x=450, y= 370)
            
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