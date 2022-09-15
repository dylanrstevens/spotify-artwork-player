
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
        self.attributes("-topmost", False)
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
    

class SettingsWindow(Tk):

    linkEntered = None
    authenticationLink = None
    enterButton = None
    toggleBind = None
    toggleUnbind = None
    authentication_label = None

    def __init__(self) -> None:
        super().__init__()
        self.geometry("400x300")
        #self['background']="black"
        self.iconbitmap('./icon256.ico')
        self.eval('tk::PlaceWindow . center')
        self.title("App")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.authentication_label = Label(self, text="")
        self.authentication_label.pack()

        #self.toggleBind = Button(self, text= "Bind to front", command=self.bindTop).pack(pady= 20)
        #self.toggleUnbind = Button(self, text= "Unbind to front", command=self.unbindTop).pack(pady= 20)
        self.linkEntered = StringVar() #Variable to determine whether the enter button was pressed or not
        self.authenticationLink = Entry(self, width=30)
        self.authenticationLink.pack()
        self.enterButton = Button(self, text= "Enter", command=lambda: self.linkEntered.set("entered"))
        self.enterButton.pack()

    def getLinkInput(self):
        if not os.path.exists(".cache"):
            self.enterButton.wait_variable(self.linkEntered)
            link = self.authenticationLink.get()
            return link
    
    def on_closing(self):
        self.destroy()

    def setRegistered(self):
        self.authentication_label.config(text="Registered")
    
    def setUnregistered(self):
        self.authentication_label.config(
            text="""Unregistered\n
After signing in, you will be redirected to 'localhost'.\n
Please copy the redirected URL from your browser and paste\n
it here to register the app with your spotify account"""
            )
    
    def removeAuthentications(self):
        self.enterButton.destroy()
        self.authenticationLink.pack_forget()