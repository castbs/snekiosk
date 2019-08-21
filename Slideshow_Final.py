from Tkinter import *
import webbrowser
import subprocess
from time import sleep

root = Tk()
frame = Frame(root)

def OpenUrl(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Slideshow.html", shell = True)

button = Button(frame, text="click.", command=OpenUrl)

OpenUrl()
root.destroy()

root.mainloop()