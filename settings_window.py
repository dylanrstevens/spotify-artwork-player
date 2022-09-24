from tkinter import Frame, TclError, Tk, Button, Entry, StringVar, Label, IntVar
import os.path
from tkinter.font import BOLD

FONT = ("Verdana", 10)
TITLE_FONT = ("Verdana", 12, BOLD)
  
class SettingsApp(Tk):

    RUNNING_LOOP = None

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.RUNNING_LOOP = True
        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.geometry("320x225")
        self.iconbitmap('./icon256.ico')
        self.eval('tk::PlaceWindow . center')
        self.title("Spotify Artwork Player")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.frames = {} 

        self.frames[HomePage] = HomePage(parent=container, controller=self)
        self.frames[AuthenticatePage] = AuthenticatePage(parent=container, controller=self)
        self.frames[InstructionsPage] = InstructionsPage(parent=container, controller=self)

        self.frames[HomePage].grid(row=0, column=0, sticky="nsew")
        self.frames[AuthenticatePage].grid(row=0, column=0, sticky="nsew")
        self.frames[InstructionsPage].grid(row=0, column=0, sticky="nsew")

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
    loginButton = None
    login_clicked = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text ="Authentication", font=TITLE_FONT)
        description = Label(self, text ="After signing in with the opened browser,\ncopy and paste the redirected link below", anchor="w", justify="left")
        title.grid(row = 1, column = 0, columnspan=4, sticky="W", pady=10)
        description.grid(row=3, column=0, columnspan=4, sticky="W")

        self.linkEntered = StringVar() #Variable to determine whether the enter button was pressed or not
        self.authenticationLink = Entry(self, width=30)
        self.authenticationLink.grid(row=4, column=0, columnspan=4, sticky="W")

        self.enterButton = Button(self, text= "Enter",
            command=lambda: self.linkEntered.set("entered"))
        self.enterButton.grid(row=5, column=0, columnspan=4, sticky="W")

        self.login_clicked = IntVar()
        self.loginButton = Button(self, text="Log In",
            command=lambda: self.login_clicked.set(1))
        self.loginButton.grid(row=2, column=0, columnspan=4, sticky="W")

        settings_button = Button(self, text ="Settings",
            command = lambda : controller.show_frame(HomePage), font=FONT)
        settings_button.grid(row = 0, column = 0, sticky="W")

        authenticate_button = Button(self, text ="Authenticate",
            command = lambda : controller.show_frame(AuthenticatePage), font=FONT)
        authenticate_button.grid(row = 0, column = 1, sticky="W")

        instructions_button = Button(self, text ="Instructions", 
            command = lambda : controller.show_frame(InstructionsPage), font=FONT)
        instructions_button.grid(row = 0, column = 2, sticky="W")

        help_button = Button(self, text ="Help", font=FONT)
        help_button.grid(row = 0, column = 3, sticky="W")

    
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
        self.RegistrationStatus = Label(self, text="", anchor="w", justify="left")
        self.RegistrationStatus.grid(row=4, column= 0, columnspan=4, sticky="W", pady=(50, 10))
        self.registeredBool = False

        title = Label(self, text ="Settings", font=TITLE_FONT)
        title.grid(row = 1, column = 0, columnspan=2, sticky="W", pady=10)

        settings_button = Button(self, text ="Settings",
            command = lambda : controller.show_frame(HomePage), font=FONT)
        settings_button.grid(row = 0, column = 0, sticky="W")

        authenticate_button = Button(self, text ="Authenticate",
            command = lambda : controller.show_frame(AuthenticatePage), font=FONT)
        authenticate_button.grid(row = 0, column = 1, sticky="W")

        instructions_button = Button(self, text ="Instructions", 
            command = lambda : controller.show_frame(InstructionsPage), font=FONT)
        instructions_button.grid(row = 0, column = 2, sticky="W")

        help_button = Button(self, text ="Help", font=FONT)
        help_button.grid(row = 0, column = 3, sticky="W")

        if os.path.exists(".cache"):
            self.setRegistered()
        else:
            self.setUnregistered()

    def setRegistered(self):
        self.RegistrationStatus.config(text="Status: Registered")
        self.registeredBool = True
    
    def setUnregistered(self):
        self.RegistrationStatus.config(text="Status: Unregistered, please follow the instructions\nby clicking the 'Authenticate' button")
        self.registeredBool = False


class InstructionsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        title = Label(self, text ="Instructions", font=TITLE_FONT)
        title.grid(row = 1, column = 0, columnspan=2, sticky="W", pady=10)

        settings_button = Button(self, text ="Settings",
            command = lambda : controller.show_frame(HomePage), font=FONT)
        settings_button.grid(row = 0, column = 0, sticky="W")

        authenticate_button = Button(self, text ="Authenticate",
            command = lambda : controller.show_frame(AuthenticatePage), font=FONT)
        authenticate_button.grid(row = 0, column = 1, sticky="W")

        instructions_button = Button(self, text ="Instructions", 
            command = lambda : controller.show_frame(InstructionsPage), font=FONT)
        instructions_button.grid(row = 0, column = 2, sticky="W")

        help_button = Button(self, text ="Help", font=FONT)
        help_button.grid(row = 0, column = 3, sticky="W")
