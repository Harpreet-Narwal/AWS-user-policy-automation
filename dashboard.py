from tkinter import *

class face:
    def __init__(self,window):
        self.window = window
        self.window.title("AWS User Automation App")
        self.window.geometry('1200x675+0+0')

window = Tk()
player = face(window)
window.mainloop()