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
        self.frames[HowToAuthenticate] = HowToAuthenticate(parent=container, controller=self)
        self.frames[HowToUse] = HowToUse(parent=container, controller=self)

        self.frames[HomePage].grid(row=0, column=0, sticky="nsew")
        self.frames[AuthenticatePage].grid(row=0, column=0, sticky="nsew")
        self.frames[InstructionsPage].grid(row=0, column=0, sticky="nsew")
        self.frames[HowToAuthenticate].grid(row=0, column=0, sticky="nsew")
        self.frames[HowToUse].grid(row=0, column=0, sticky="nsew")

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

        how_to_authenticate = Button(self, text="How to register",
            command = lambda : controller.show_frame(HowToAuthenticate))
        how_to_authenticate.grid(row=2, column=0, columnspan=2, sticky="W")

        how_to_use = Button(self, text="How to use",
            command = lambda : controller.show_frame(HowToUse))
        how_to_use.grid(row=3, column=0, columnspan=2, sticky="W")


class HowToAuthenticate(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)

        title = Label(self, text ="How To Register", font=TITLE_FONT)
        title.grid(row = 0, column = 0, columnspan=1, sticky="W")

        description = Label(self, text=
"""In order to use the Spotify Artwork Player, you must
register the app with your spotify account. This is required
in order to read your currently playing song.

1. Click 'Authenticate' and begin by clicking 'Log in'
2. Log into spotify, using the opened webbrowser page
3. After approving the app to read your current song
data, you will be redirected to 'localhost'.
4. Copy the entire URL of this page, paste into the
text input, and hit enter.""", anchor="w", justify="left")
        description.grid(row=1, column=0, columnspan=4, sticky="W")

        back_button = Button(self, text="Back",
            command = lambda : controller.show_frame(InstructionsPage))
        back_button.grid(row=2, column=0, sticky="W", pady=2)

class HowToUse(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)

        title = Label(self, text ="How To Use", font=TITLE_FONT)
        title.grid(row = 0, column = 0, columnspan=1, sticky="W")

        description = Label(self, text=
"""After registering the app, you will see a blank square
open on your screen. Begin by opening up spotify, playing
a song, and the album cover of that song will appear.

1.'Bind to front' will place the album cover ontop of all 
other windows.
2. 'Unbind to front' will give priority to other windows.
3. Move the album cover around by clicking on it and 
dragging it accross your screen.""", anchor="w", justify="left")
        description.grid(row=1, column=0, columnspan=4, sticky="W")

        back_button = Button(self, text="Back",
            command = lambda : controller.show_frame(InstructionsPage))
        back_button.grid(row=2, column=0, sticky="W", pady=2)