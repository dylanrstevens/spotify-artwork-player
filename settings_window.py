import time
from tkinter import Frame, TclError, Tk, Button, Entry, StringVar, Label
import os.path
from PIL import ImageTk, Image
  
class SettingsApp(Tk):

    RUNNING_LOOP = None

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.RUNNING_LOOP = True
        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.geometry("400x300")
        self.iconbitmap('./icon256.ico')
        self.eval('tk::PlaceWindow . center')
        self.title("App")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)


        self.frames = {} 

        self.frames[HomePage] = HomePage(parent=container, controller=self)
        self.frames[AuthenticatePage] = AuthenticatePage(parent=container, controller=self)

        self.frames[HomePage].grid(row=0, column=0, sticky="nsew")
        self.frames[AuthenticatePage].grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def on_closing(self):
        self.destroy()
        self.RUNNING_LOOP = False


class AuthenticatePage(Frame):

    linkEntered = None
    authenticationLink = None
    enterButton = None
    authentication_label = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text ="Authentication")
        description = Label(self, text ="After signing in with the opened browser,\ncopy and paste the redirected link below")
        title.grid(row = 0, column = 0)
        description.grid(row=1, column=0)

        self.linkEntered = StringVar() #Variable to determine whether the enter button was pressed or not
        self.authenticationLink = Entry(self, width=30)
        self.authenticationLink.grid(row=2, column=0)
        self.enterButton = Button(self, text= "Enter", command=lambda: self.linkEntered.set("entered"))
        self.enterButton.grid(row=3, column=0)

        button1 = Button(self, text ="Settings",
            command = lambda : controller.show_frame(HomePage))
        button1.grid(row = 4, column = 0)

    
    def getLinkInput(self):
        if not os.path.exists(".cache"):
            self.enterButton.wait_variable(self.linkEntered)
            link = self.authenticationLink.get()
            return link

  

class HomePage(Frame):
     
    RegistrationStatus = None
    registeredBool = None

    def __init__(self, parent, controller): 
        Frame.__init__(self, parent)
        self.RegistrationStatus = Label(self, text="")
        self.RegistrationStatus.grid(row=0, column= 1)
        self.registeredBool = False

        label = Label(self, text ="Settings")
        label.grid(row = 0, column = 0)

        button1 = Button(self, text ="Authenticate",
                            command = lambda : controller.show_frame(AuthenticatePage))
        button1.grid(row = 1, column = 0)

        if os.path.exists(".cache"):
            self.setRegistered()
        else:
            self.setUnregistered()

    def setRegistered(self):
        self.RegistrationStatus.config(text="Status: Registered")
        self.registeredBool = True
    
    def setUnregistered(self):
        self.RegistrationStatus.config(text="Status: Unregistered, please follow\ninstructions by clicking the 'Authenticate' button")
        self.registeredBool = False


#app = SettingsApp()
#app.mainloop()
