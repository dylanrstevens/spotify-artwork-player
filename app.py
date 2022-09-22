from os import link
import os.path
from display_window import DisplayWindow
from settings_window import SettingsApp, AuthenticatePage, HomePage
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.request
from tkinter import Label, TclError, Button
from PIL import ImageTk, Image

def main():
    
    
    app = SettingsApp()
    #print(app.frames[AuthenticatePage].getLinkInput())
    
    
    scope = "user-read-currently-playing"
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, instance=app))
    try:
        current_image = spotify.current_user_playing_track()["item"]["album"]["images"][1]["url"]
    except:
        current_image = ""
    
    app.frames[HomePage].setRegistered()

    display = DisplayWindow()
    
    if (app.frames[HomePage].registeredBool == True):
        toggleBind = Button(app.frames[HomePage], text= "Bind to front", command=display.setBindTop)
        toggleBind.grid(row=2, column=0)
        toggleUnbind = Button(app.frames[HomePage], text= "Unbind to front", command=display.setUnbindTop)
        toggleUnbind.grid(row=3, column=0)

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
                display.update_img()
        except TclError as ApplicationDestroyed:
            LOOP_ACTIVE = False
        except TypeError as NoSongFound:
            pass
            #print(NoSongFound)
        except:
            pass
            #print(e)

if __name__ == "__main__":
    main()