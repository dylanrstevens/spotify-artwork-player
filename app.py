from requests import ConnectionError
from display_window import DisplayWindow
from settings_window import SettingsApp, AuthenticatePage, HomePage
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.request
from tkinter import TclError, Button, W
from PIL import ImageTk, Image
from envvars import client_id, client_secret, redirect_uri

def main():
    
    
    app = SettingsApp()
    #print(app.frames[AuthenticatePage].getLinkInput())
    
    
    scope = "user-read-currently-playing"
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, instance=app))
    try:
        current_image = spotify.current_user_playing_track()["item"]["album"]["images"][1]["url"]
    except:
        current_image = ""
    
    app.frames[HomePage].setRegistered()

    display = DisplayWindow()
    
    if (app.frames[HomePage].registeredBool == True):
        toggleBind = Button(app.frames[HomePage], text= "Bind to front", command=display.setBindTop)
        toggleBind.grid(row=2, column=0, columnspan=2, sticky=W)
        toggleUnbind = Button(app.frames[HomePage], text= "Unbind to front", command=display.setUnbindTop)
        toggleUnbind.grid(row=3, column=0, columnspan=2, sticky=W)

    #APP & DISPLAY LOOP TO GET ALBUM COVER EVERY TIME SONG CHANGES
    last_song = ""
    while app.RUNNING_LOOP:
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
            pass
        except TypeError as NoSongFound:
            #! DOES NOT BREAK LOOP AS THIS ERROR WILL BE RAISED IN BETWEEN SONG SELECTIONS BRIEFLY
            pass
        except ConnectionError as NoConnectionEstablished:
            #! THIS ERROR IS RAISED WHEN THERE IS NO CONNECTION TO INTERNET (HTTP CANNOT MAKE A CONNECTION)
            pass
        except:
            pass
            

if __name__ == "__main__":
    try:
        main()
    except:
        pass