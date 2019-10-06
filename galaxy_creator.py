from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import random

def createWallpaper(givenRes):

    # Decide iRes and jRes from user input in window
    # split string by 'x' delimiter, convert to int with map function
    # store into list b/c map returns lazy object in Python3
    res = list(map(int, givenRes.split("x")))

    # Sets up background to screen resolution size, default black
    background = Image.new('RGB', (res[0], res[1]), color=(0, 0, 0))

    # Chooses font for "." which is used to represent a star
    fnt = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 8)

    # Draws image with background as base
    d = ImageDraw.Draw(background)

    # Iterates through each pixel to determine if star goes there
    for i in range(0, res[0]):
        for j in range(0, res[1]):

            randInt = random.randint(1, 1001)

            if j < 324 and randInt > 999:
                d.text((i, j), ".", font=fnt, fill=(255, 255, 255))
            elif j >= 324 and j < 648 and randInt > 996:
                d.text((i, j), ".", font=fnt, fill=(255, 255, 255))
            elif j >= 648 and j < 756 and randInt > 995:
                d.text((i, j), ".", font=fnt, fill=(255, 255, 255))
            else:
                if randInt > 996:
                    d.text((i, j), ".", font=fnt, fill=(255, 255, 255))

    # Saves image to png file as specified name
    background.save('galaxy_wallpaper.png')

# Window containing Label, OptionMenu, and Button
class window (Frame):
    # Initializer to inherit from superclass Frame, set location of Widgets
    def __init__ (self, master):
        super(window, self).__init__(master)
        self.grid(sticky=W, padx=10, pady=10)

        # Label Widget
        Label (self,
              text="Select Your Resolution"
              ).grid(row=0, column=0, sticky=E)

        # Object for OptionMenu with default value, stores resolution(s)
        self.res = StringVar()
        self.res.set("1920x1080")

        # OptionMenu Widget
        OptionMenu (self, self.res,
                    "320x480",
                    "728x1024",
                    "1024x768",
                    "1280x800",
                    "1280x1024",
                    "1366x768",
                    "1440x900",
                    "1600x1050",
                    "1680x1050",
                    "1920x1080",
                    ).grid(row=0, column=1, sticky="we")

        # Button Widget, activiates creates wallpaper
        Button (self,
                text="Make Wallpaper!",
                command=createWallpaper(self.res.get()) # passes string value of OptionMenu Object
                ).grid(row=0, column=2, sticky="we", pady=5)

# Main
# Sets up GUI Window
root = Tk()
root.title("Galaxy Wallpaper Generator")
root.geometry("350x50")
window = window(root)
root.mainloop() # Keeps program running
