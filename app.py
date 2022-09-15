from os import link
import os.path
from display_window import DisplayWindow, SettingsWindow
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.request
from tkinter import Label, TclError, Button
from PIL import ImageTk, Image

def main():
    
    
    app = SettingsWindow()
    #print(app.getLinkInput())
    if os.path.exists(".cache"):
        app.setRegistered()
    else:
        app.setUnregistered()
    
    scope = "user-read-currently-playing"
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, instance=app))
    try:
        current_image = spotify.current_user_playing_track()["item"]["album"]["images"][1]["url"]
    except:
        current_image = ""
    
    display = DisplayWindow()
    toggleBind = Button(app, text= "Bind to front", command=display.setBindTop).pack()
    toggleUnbind = Button(app, text= "Unbind to front", command=display.setUnbindTop).pack()

    app.setRegistered()
    app.removeAuthentications()

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