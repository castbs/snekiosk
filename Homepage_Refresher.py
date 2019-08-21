import subprocess
import Tkinter as tk
from Tkinter import *
import os
import sys
import time
from time import sleep, gmtime, strftime

button_master = Tk()
button_master.config(width=500, height=500)
canvas = Canvas(button_master, bg="white")
button_master.configure(bg='white')

def refresh():
    current_time = ''
    time_clock = Label(button_master, font = ('lato', 75, 'bold'), fg='red', bg='white')
    time_clock.place(x = 175, y = 350)
    day_clock = Label(button_master, font = ('lato', 60, 'bold'), fg='red', bg='white')
    day_clock.place(x = 300, y = 475)
    current_time = time.strftime('%I:%M:%S %p')
    current_day = time.strftime('%m/%d/%y')
    time_clock.config(text = current_time)
    day_clock.config(text = current_day)
    
    #button_master.destroy('python Homepage_with_CSV3.py')
    os.system('python Homepage_with_CSV4.py')
    
    time_clock.after(602000, refresh) #600000 is 10 minutes

os.system('python Homepage_with_CSV4.py')
refresh()
button_master.mainloop()