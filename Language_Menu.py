import subprocess
import Tkinter as tk
from Tkinter import *
'''
        weather_window1 = tk.Toplevel(button_master)
        #weather_window1.attributes("-fullscreen", True)
        #tk.bind("<Escape>", fullscreen_off)
        def close_weather_details1():
            button_master.destroy()
            #weather_window1 = tk.Toplevel(button_master)
            #weather_window1.attributes("-fullscreen", True)
            #k.bind("<Escape>", fullscreen_off)
        weather_window1_close_button = Button(button_master, text="Return to Home Screen", background = 'red', command=close_weather_details1)
        weather_window1_close_button.config(font=('lato', 16, 'bold'))
        weather_window1_close_button.config(height = 2, width = 10)
        weather_window1_close_button.configure(foreground = 'white')
        weather_window1_close_button.place(x = 10, y = 10)
        canvas.tag_raise(weather_window1_close_button)
'''

button_master = Tk()
button_master.config(width=500, height=500)
button_font = ('lato', 20, 'bold')
canvas = Canvas(button_master, bg="white")
button_master.configure(bg='white')
button_master.attributes("-fullscreen", True)


def close_language_menu():
    button_master.destroy()
language_menu_close_button = Button(button_master, text="Return to Home Screen", background = 'red', command=close_language_menu)
language_menu_close_button.config(font=('lato', 16, 'bold'))
language_menu_close_button.config(height = 2, width = 20)
language_menu_close_button.configure(foreground = 'white')
language_menu_close_button.place(x = 10, y = 10)
canvas.tag_raise(language_menu_close_button)

def open_Latin_language_trivia(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Latin_Language_Trivia_HTML_Page.html", shell = True)
Latin_button = Button(button_master, text="Latin", background = 'red', command=open_Latin_language_trivia)
Latin_button.config(font=button_font)
Latin_button.config(height = 3, width = 50)
Latin_button.configure(foreground = 'white')
Latin_button.place(x = 500, y = 40)

def open_French_language_trivia(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/French_Language_Trivia_HTML_Page.html", shell = True)
French_button = Button(button_master, text="French", background = 'red', command=open_French_language_trivia)
French_button.config(font=button_font)
French_button.config(height = 3, width = 50)
French_button.configure(foreground = 'white')
French_button.place(x = 500, y = 200)

def open_Mandarin_language_trivia(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Mandarin_Language_Trivia_HTML_Page.html", shell = True)
Mandarin_button = Button(button_master, text="Mandarin", background = 'red', command=open_Mandarin_language_trivia)
Mandarin_button.config(font=button_font)
Mandarin_button.config(height = 3, width = 50)
Mandarin_button.configure(foreground = 'white')
Mandarin_button.place(x = 500, y = 360)

def open_Spanish_language_trivia(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Spanish_Language_Trivia_HTML_Page.html", shell = True)
Spanish_button = Button(button_master, text="Spanish", background = 'red', command=open_Spanish_language_trivia)
Spanish_button.config(font=button_font)
Spanish_button.config(height = 3, width = 50)
Spanish_button.configure(foreground = 'white')
Spanish_button.place(x = 500, y = 520)

def open_German_language_trivia(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/German_Language_Trivia_HTML_Page.html", shell = True)
German_button = Button(button_master, text="German", background = 'red', command=open_German_language_trivia)
German_button.config(font=button_font)
German_button.config(height = 3, width = 50)
German_button.configure(foreground = 'white')
German_button.place(x = 500, y = 680)

def open_Greek_language_trivia(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Greek_Language_Trivia_HTML_Page.html", shell = True)
Greek_button = Button(button_master, text="Greek", background = 'red', command=open_Greek_language_trivia)
Greek_button.config(font=button_font)
Greek_button.config(height = 3, width = 50)
Greek_button.configure(foreground = 'white')
Greek_button.place(x = 500, y = 830)


button_master.mainloop()