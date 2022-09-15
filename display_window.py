from tkinter import Toplevel, Tk, Button, Entry, StringVar
import os.path

class DisplayWindow(Toplevel):
    """
    CLASS FOR IMAGE WINDOW TO ALLOW FOR BORDLERLESS DRAGABLE FRAME
    """
    def __init__(self,master=None):
        Toplevel.__init__(self,master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)

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


class SettingsWindow(Tk):

    linkEntered = None
    authenicationLink = None
    enterButton = None
    toggleBind = None
    toggleUnbind = None

    def __init__(self) -> None:
        super().__init__()
        self.geometry("400x300")
        #self['background']="black"
        self.iconbitmap('./icon256.ico')
        self.eval('tk::PlaceWindow . center')
        self.title("App")
        self.resizable(False, False)

        self.toggleBind = Button(self, text= "Bind to front", command=DisplayWindow.setBindTop).pack(pady= 20)
        self.toggleUnbind = Button(self, text= "Unbind to front", command=DisplayWindow.setUnbindTop).pack(pady= 20)
        self.linkEntered = StringVar() #Variable to determine whether the enter button was pressed or not
        self.authenticationLink = Entry(self, width=30)
        self.authenticationLink.pack(pady=20)
        self.enterButton = Button(self, text= "Enter", command=lambda: self.linkEntered.set("entered"))
        self.enterButton.pack(pady= 20)

    def getLinkInput(self):
        if not os.path.exists(".cache"):
            self.enterButton.wait_variable(self.linkEntered)
            link = self.authenticationLink.get()
            return link

