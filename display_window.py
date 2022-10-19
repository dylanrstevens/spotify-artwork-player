
from tkinter import Toplevel, Tk, Button, Entry, StringVar, Label
import os.path
from PIL import ImageTk, Image

class DisplayWindow(Toplevel):
    
    img = ""
    panel = None

    def __init__(self,master=None):
        Toplevel.__init__(self,master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)

        self.geometry("300x300")
        self.maxsize(300,300)
        self.attributes("-topmost", True)
        self.initiateImage()
        self.panel = Label(self, image = self.img)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")

    def dragwin(self,event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self._offsetx = event.x
        self._offsety = event.y

    def setBindTop(self):
        self.attributes("-topmost", True)
    
    def setUnbindTop(self):
        self.attributes("-topmost", False)

    def update_img(self):
        self.img = ImageTk.PhotoImage(Image.open("art.png"))
        self.panel.configure(image=self.img)
        self.panel.image = self.img

    def initiateImage(self):
        try:
            self.img = ImageTk.PhotoImage(Image.open("art.png"))
        except:
            self.img = ""
