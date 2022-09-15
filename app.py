from os import link
import os.path
from display_window import DisplayWindow, SettingsWindow
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.request
from tkinter import StringVar, TclError, Label, Button, Entry
from PIL import ImageTk, Image

scope = "user-read-currently-playing"
#spotifyObject = SpotifyAuthBase()
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#FUNCTION TO TOGGLE DISPLAY TO BE TOPMOST
def bindTop():
    display.attributes("-topmost", True)

#FUNCTION TO TOGGLE DISPLAY TO BE NOT TOPMOST (REGULAR WINDOW MANAGEMENT)
def unbindTop():
    display.attributes("-topmost", False)

#UPDATE IMAGE FUNCTION
def update_img():
    img = ImageTk.PhotoImage(Image.open("art.png"))
    panel.configure(image=img)
    panel.image = img

#FUNCTION TO DEFINE WINDOW MANAGER CLOSING ('X' BUTTON PRESSED ON APP)
def on_closing():
    app.destroy()


#APP INITIATION
app = SettingsWindow()





print(app.getLinkInput())



    

app.protocol("WM_DELETE_WINDOW", on_closing)

#DISPLAY INITIATION
display = DisplayWindow()
try:
    img = ImageTk.PhotoImage(Image.open("art.png"))
except:
    img = ""
display.geometry("300x300")
display.maxsize(300,300)
display.attributes("-topmost", False)
panel = Label(display, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


#APP & DISPLAY LOOP TO GET ALBUM COVER EVERY TIME SONG CHANGES
last_song = ""
LOOP_ACTIVE = True
while LOOP_ACTIVE:
    try:
        #print("tried")
        app.update()
        display.update()
        current_image = spotify.current_user_playing_track()["item"]["album"]["images"][1]["url"]
        current_song = current_image
        #print(current_image)
        if (last_song != current_song):
            #print("downloaded")
            urllib.request.urlretrieve(current_image, "art.png")
            last_song = current_song
            update_img()
    except TclError as ApplicationDestroyed:
        LOOP_ACTIVE = False
    except TypeError as NoSongFound:
        pass
    except:
        pass
