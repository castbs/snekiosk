import subprocess
import Tkinter as tk
from Tkinter import *
import os
import sys
import time
from time import sleep, gmtime, strftime
from PIL import Image
import picamera
import requests
import csv
import threading
from threading import Timer

def find_day_or_night(weather_month, weather_hour):
    weather_hour = int(weather_hour)
    if weather_month == '01':
        if weather_hour > 7 and weather_hour < 17: time_of_day = 'day'
        else: time_of_day = 'night'
    elif weather_month == '02':
        if weather_hour > 7 and weather_hour < 17: time_of_day = 'day'
        else: time_of_day = 'night'
    if weather_month == '03':
        if weather_hour > 7 and weather_hour < 12: time_of_day = 'day'
        else: time_of_day = 'night'
    elif weather_month == '03':
        if weather_hour > 7 and weather_hour < 19: time_of_day = 'day'
        else: time_of_day = 'night'
    elif weather_month == '04':
        if weather_hour > 6 and weather_hour < 19: time_of_day = 'day'
        else: time_of_day = 'night'
    elif weather_month == '05':
        if weather_hour > 6 and weather_hour < 20: time_of_day = 'day'
        else: time_of_day = 'night'
    if weather_month == '06':
        if weather_hour > 5 and weather_hour < 20: time_of_day = 'day'
        else: time_of_day = 'night'
    elif weather_month == '07':
        if weather_hour > 6 and weather_hour < 20: time_of_day = 'day'
        else: time_of_day = 'night'
    elif weather_month == '08':
        if weather_hour > 6 and weather_hour < 20: time_of_day = 'day'
        else: time_of_day = 'night'
    if weather_month == '09':
        if weather_hour > 7 and weather_hour < 19: time_of_day = 'day'
        else: time_of_day = 'night'
    elif weather_month == '10':
        if weather_hour > 7 and weather_hour < 18: time_of_day = 'day'
        else: time_of_day = 'night'
    elif weather_month == '11':
        if weather_hour > 7 and weather_hour < 17: time_of_day = 'day'
        else: time_of_day = 'night'
    if weather_month == '12':
        if weather_hour > 7 and weather_hour < 16: time_of_day = 'day'
        else: time_of_day = 'night'
    else: time_of_day = 'day'
    return time_of_day

button_master = Tk()
button_master.title("BREARLEY KIOSK")
button_master.config(width=500, height=500)
button_master.attributes("-fullscreen", True)
def FALSE_fullscreen(event): button_master.attributes("-fullscreen", False)
button_master.bind("<Escape>", FALSE_fullscreen)
def DESTROY_fullscreen(event): button_master.destroy()
button_master.bind("<Return>", DESTROY_fullscreen)
button_font = ('lato', 20, 'bold')
temperature_font = ('lato', 30, 'bold')
weather_description_font = ('lato', 16, 'bold')
weather_button_font = ('lato', 16, 'bold')

crest_filename = PhotoImage(file = "/home/pi/Desktop/Brearley_crest.png")
crest_background_label = Label(image=crest_filename)
crest_background_label.place(x=300, y=50, relwidth=0.156, relheight=0.3)

canvas = Canvas(button_master, bg="white")

current_time = ''
time_clock = Label(button_master, font = ('lato', 75, 'bold'), fg='red', bg='white')
time_clock.place(x = 175, y = 350)
day_clock = Label(button_master, font = ('lato', 60, 'bold'), fg='red', bg='white')
day_clock.place(x = 300, y = 475)

    
api_address = 'http://api.openweathermap.org/data/2.5/forecast?appid=665c0a4c70ee4aecec2fd415645cc9fc&q='
city = "new york"
url = api_address + city
json_data = requests.get(url).json()    

day = 1
last_day_time_checked = ''

'''
print(int(((box1["main"]["temp"]) * 9/5) - 459.67))
print(box1["weather"][0]["main"])
print(box1["weather"][0]["description"])
print(box1["dt_txt"])
'''
degrees_sign = (u'\u00b0'+ " F")

sunny1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/sunny.png")
clear_night1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/clear_night.png")
cloudy1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/cloudy.png")
partly_cloudy_day1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/partly_cloudy_day.png")
partly_cloudy_night1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/partly_cloudy_night.png")
heavy_rain1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/heavy_rain.png")
light_rain1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/light_rain.png")
thunder_with_rain1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/thunder_with_rain.png")
thunder_without_rain1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/thunder_without_rain.png")
snowy1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/snowy.png")
windy1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/windy.png")
foggy1 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/foggy.png")

sunny2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/sunny.png")
clear_night2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/clear_night.png")
cloudy2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/cloudy.png")
partly_cloudy_day2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/partly_cloudy_day.png")
partly_cloudy_night2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/partly_cloudy_night.png")
heavy_rain2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/heavy_rain.png")
light_rain2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/light_rain.png")
thunder_with_rain2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/thunder_with_rain.png")
thunder_without_rain2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/thunder_without_rain.png")
snowy2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/snowy.png")
windy2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/windy.png")
foggy2 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/foggy.png")

sunny3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/sunny.png")
clear_night3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/clear_night.png")
cloudy3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/cloudy.png")
partly_cloudy_day3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/partly_cloudy_day.png")
partly_cloudy_night3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/partly_cloudy_night.png")
heavy_rain3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/heavy_rain.png")
light_rain3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/light_rain.png")
thunder_with_rain3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/thunder_with_rain.png")
thunder_without_rain3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/thunder_without_rain.png")
snowy3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/snowy.png")
windy3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/windy.png")
foggy3 = PhotoImage(file = "/home/pi/Desktop/Weather Icons/foggy.png")



def change_weather_picture():
    #THE 1st BOX
    weather1_frame1 = Frame(button_master, highlightbackground="red", highlightthickness=20, width=200, height=300, bd= 0, bg="white")
    weather1_frame1.place(x = 30, y = 595)
    weather1_frame2 = Frame(button_master, highlightbackground="red", highlightthickness=20, width=200, height=100, bd= 0, bg="white")
    weather1_frame2.place(x = 30, y = 595)
    canvas.tag_lower(weather1_frame2)
    box1 = json_data["list"][0]
    sunny_label1 = Label(image=sunny1)
    clear_night_label1 = Label(image=clear_night1)
    cloudy_label1 = Label(image=cloudy1)
    partly_cloudy_day_label1 = Label(image=partly_cloudy_day1)
    partly_cloudy_night_label1 = Label(image=partly_cloudy_night1)
    heavy_rain_label1 = Label(image=heavy_rain1)
    light_rain_label1 = Label(image=light_rain1)
    thunder_with_rain_label1 = Label(image=thunder_with_rain1)
    thunder_without_rain_label1 = Label(image=thunder_without_rain1)
    snowy_label1 = Label(image=snowy1)
    windy_label1 = Label(image=windy1)
    foggy_label1 = Label(image=foggy1)
    weather_time1 = box1["dt_txt"]
    weather_day1 = str(weather_time1).split(" ")[0].split("-")[1] + "/" + str(weather_time1).split(" ")[0].split("-")[2]
    weather_hour_raw1 = str(weather_time1).split(" ")[1].split(":")[0]
    if int(weather_hour_raw1) == 0: weather_hour1 = "12 AM"
    elif int(weather_hour_raw1) < 12: weather_hour1 = str(int(weather_hour_raw1)) + " AM"
    elif int(weather_hour_raw1) == 12: weather_hour1 = "12 PM"
    elif int(weather_hour_raw1) > 12: weather_hour1 = str(int(weather_hour_raw1) - 12) + " PM"
    weather_month = str(weather_time1).split(" ")[0].split("-")[1]
    time_of_day1 = find_day_or_night(weather_month, weather_hour_raw1)
    weather_picture1 = sunny_label1
    '''
    if box1["weather"][0]["main"] == "Thunderstorm":
        if box1["weather"][0]["description"] == "thunderstorm with light rain": thunder_without_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "thunderstorm with rain": thunder_with_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "thunderstorm with heavy rain": thunder_with_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "light thunderstorm": thunder_without_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "thunderstorm": thunder_with_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "heavy thunderstorm": thunder_with_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "ragged thunderstorm": thunder_with_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "thunderstorm with light drizzle": thunder_without_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "thunderstorm with drizzle": thunder_without_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        else: thunder_with_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Rain": heavy_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Drizzle": light_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Clear":
        if time_of_day1 == 'day': sunny_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        else: clear_night_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Snow": snowy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Clouds":
        if box1["weather"][0]["description"] == "few clouds":
            if time_of_day1 == 'day': partly_cloudy_day_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
            else: partly_cloudy_night_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "scattered clouds":
            if time_of_day1 == 'day': partly_cloudy_day_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
            else: partly_cloudy_night_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        elif box1["weather"][0]["description"] == "broken clouds": cloudy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
        else: cloudy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Mist": foggy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Smoke": windy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Haze": foggy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Dust": windy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Ash": windy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    elif box1["weather"][0]["main"] == "Squall": heavy_rain_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    else: windy_label1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    '''
    if box1["weather"][0]["main"] == "Thunderstorm":
        if box1["weather"][0]["description"] == "thunderstorm with light rain": weather_picture1 = thunder_without_rain_label1 
        elif box1["weather"][0]["description"] == "thunderstorm with rain": weather_picture1 = thunder_with_rain_label1 
        elif box1["weather"][0]["description"] == "thunderstorm with heavy rain": weather_picture1 = thunder_with_rain_label1 
        elif box1["weather"][0]["description"] == "light thunderstorm": weather_picture1 = thunder_without_rain_label1 
        elif box1["weather"][0]["description"] == "thunderstorm": weather_picture1 = thunder_with_rain_label1 
        elif box1["weather"][0]["description"] == "heavy thunderstorm": weather_picture1 = thunder_with_rain_label1 
        elif box1["weather"][0]["description"] == "ragged thunderstorm": weather_picture1 = thunder_with_rain_label1 
        elif box1["weather"][0]["description"] == "thunderstorm with light drizzle": weather_picture1 = thunder_without_rain_label1 
        elif box1["weather"][0]["description"] == "thunderstorm with drizzle": weather_picture1 = thunder_without_rain_label1 
        else: weather_picture1 = thunder_with_rain_label1 
    elif box1["weather"][0]["main"] == "Rain": weather_picture1 = heavy_rain_label1 
    elif box1["weather"][0]["main"] == "Drizzle": weather_picture1 = light_rain_label1 
    elif box1["weather"][0]["main"] == "Clear":
        if time_of_day1 == 'day': weather_picture1 = sunny_label1 
        else: clear_night_label1 
    elif box1["weather"][0]["main"] == "Snow": weather_picture1 = snowy_label1 
    elif box1["weather"][0]["main"] == "Clouds":
        if box1["weather"][0]["description"] == "few clouds":
            if time_of_day1 == 'day': weather_picture1 = partly_cloudy_day_label1 
            else: weather_picture1 = partly_cloudy_night_label1 
        elif box1["weather"][0]["description"] == "scattered clouds":
            if time_of_day1 == 'day': weather_picture1 = partly_cloudy_day_label1 
            else: weather_picture1 = partly_cloudy_night_label1 
        elif box1["weather"][0]["description"] == "broken clouds": weather_picture1 = cloudy_label1 
        else: weather_picture1 = cloudy_label1 
    elif box1["weather"][0]["main"] == "Mist": weather_picture1 = foggy_label1 
    elif box1["weather"][0]["main"] == "Smoke": weather_picture1 = windy_label1 
    elif box1["weather"][0]["main"] == "Haze": weather_picture1 = foggy_label1 
    elif box1["weather"][0]["main"] == "Dust": weather_picture1 = windy_label1 
    elif box1["weather"][0]["main"] == "Ash": weather_picture1 = windy_label1 
    elif box1["weather"][0]["main"] == "Squall": weather_picture1 = heavy_rain_label1 
    else: weather_picture1 = windy_label1 
    weather_picture1.place(x=85, y=695, relwidth=0.05, relheight=0.1)
    
    weather_time1 = weather_hour1 + "    " + weather_day1
    def open_weather_details1(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Weather_Details_HTML_Page.html", shell = True)
    weather_details_button1 = Button(button_master, text=weather_time1, background = 'white', command=open_weather_details1)
    weather_details_button1.config(font=('lato', 16, 'bold'))
    weather_details_button1.config(height = 2, width = 10)
    weather_details_button1.configure(foreground = 'red')
    weather_details_button1.place(x = 130, y = 645, anchor="center")
    canvas.tag_raise(weather_details_button1)
    temperature1 = int(((box1["main"]["temp"]) * 9/5) - 459.67)
    temperature_label1 = Label(text=str(temperature1)+degrees_sign)
    temperature_label1.place(x=130, y=848, anchor="center")
    temperature_label1.config(font=temperature_font, foreground='red', bg='white')
    weather_description1 = box1["weather"][0]["main"]
    weather_description_label1 = Label(text=weather_description1)
    weather_description_label1.place(x=130, y=808, anchor="center")
    weather_description_label1.config(font=weather_description_font, foreground='red', bg='white')

    #THE 2nd BOX
    weather2_frame1 = Frame(button_master, highlightbackground="red", highlightthickness=20, width=200, height=300, bd= 0, bg="white")
    weather2_frame1.place(x = 250, y = 595)
    weather2_frame2 = Frame(button_master, highlightbackground="red", highlightthickness=20, width=200, height=100, bd= 0, bg="white")
    weather2_frame2.place(x = 250, y = 595)
    box2 = json_data["list"][1]
    sunny_label2 = Label(image=sunny2)
    clear_night_label2 = Label(image=clear_night2)
    cloudy_label2 = Label(image=cloudy2)
    partly_cloudy_day_label2 = Label(image=partly_cloudy_day2)
    partly_cloudy_night_label2 = Label(image=partly_cloudy_night2)
    heavy_rain_label2 = Label(image=heavy_rain2)
    light_rain_label2 = Label(image=light_rain2)
    thunder_with_rain_label2 = Label(image=thunder_with_rain2)
    thunder_without_rain_label2 = Label(image=thunder_without_rain2)
    snowy_label2 = Label(image=snowy2)
    windy_label2 = Label(image=windy2)
    foggy_label2 = Label(image=foggy2)
    weather_time2 = box2["dt_txt"]
    weather_day2 = str(weather_time2).split(" ")[0].split("-")[1] + "/" + str(weather_time2).split(" ")[0].split("-")[2]
    weather_hour_raw2 = str(weather_time2).split(" ")[1].split(":")[0]
    if int(weather_hour_raw2) == 0: weather_hour2 = "12 AM"
    elif int(weather_hour_raw2) < 12: weather_hour2 = str(int(weather_hour_raw2)) + " AM"
    elif int(weather_hour_raw2) == 12: weather_hour2 = "12 PM"
    elif int(weather_hour_raw2) > 12: weather_hour2 = str(int(weather_hour_raw2) - 12) + " PM"
    weather_month2 = str(weather_time2).split(" ")[0].split("-")[1]
    time_of_day2 = find_day_or_night(weather_month2, weather_hour_raw2)
    if box2["weather"][0]["main"] == "Thunderstorm":
        if box2["weather"][0]["description"] == "thunderstorm with light rain": thunder_without_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "thunderstorm with rain": thunder_with_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "thunderstorm with heavy rain": thunder_with_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "light thunderstorm": thunder_without_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "thunderstorm": thunder_with_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "heavy thunderstorm": thunder_with_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "ragged thunderstorm": thunder_with_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "thunderstorm with light drizzle": thunder_without_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "thunderstorm with drizzle": thunder_without_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        else: thunder_with_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Rain": heavy_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Drizzle": light_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Clear":
        if time_of_day2 == 'day': sunny_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        else: clear_night_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Snow": snowy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Clouds":
        if box2["weather"][0]["description"] == "few clouds":
            if time_of_day2 == 'day': partly_cloudy_day_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
            else: partly_cloudy_night_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "scattered clouds":
            if time_of_day2 == 'day': partly_cloudy_day_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
            else: partly_cloudy_night_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        elif box2["weather"][0]["description"] == "broken clouds": cloudy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
        else: cloudy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Mist": foggy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Smoke": windy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Haze": foggy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Dust": windy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Ash": windy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    elif box2["weather"][0]["main"] == "Squall": heavy_rain_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    else: windy_label2.place(x=310, y=695, relwidth=0.05, relheight=0.1)
    def open_weather_details2(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Weather_Details_HTML_Page.html", shell = True)
    weather_details_button2 = Button(button_master, text=weather_hour2 + "    " + weather_day2, background = 'white', command=open_weather_details2)
    weather_details_button2.config(font=('lato', 16, 'bold'))
    weather_details_button2.config(height = 2, width = 10)
    weather_details_button2.configure(foreground = 'red')
    weather_details_button2.place(x = 350, y = 645, anchor="center")
    canvas.tag_raise(weather_details_button2)
    temperature2 = int(((box2["main"]["temp"]) * 9/5) - 459.67)
    temperature_label2 = Label(text=str(temperature2)+degrees_sign)
    temperature_label2.place(x=350, y=848, anchor="center")
    temperature_label2.config(font=temperature_font, foreground='red', bg='white')
    weather_description2 = box2["weather"][0]["main"]
    weather_description_label2 = Label(text=weather_description2)
    weather_description_label2.place(x=350, y=808, anchor="center")
    weather_description_label2.config(font=weather_description_font, foreground='red', bg='white')

    #THE 3rd BOX
    weather3_frame1 = Frame(button_master, highlightbackground="red", highlightthickness=20, width=200, height=300, bd= 0, bg="white")
    weather3_frame1.place(x = 470, y = 595)
    weather3_frame2 = Frame(button_master, highlightbackground="red", highlightthickness=20, width=200, height=100, bd= 0, bg="white")
    weather3_frame2.place(x = 470, y = 595)
    box3 = json_data["list"][2]
    sunny_label3 = Label(image=sunny3)
    clear_night_label3 = Label(image=clear_night3)
    cloudy_label3 = Label(image=cloudy3)
    partly_cloudy_day_label3 = Label(image=partly_cloudy_day3)
    partly_cloudy_night_label3 = Label(image=partly_cloudy_night3)
    heavy_rain_label3 = Label(image=heavy_rain3)
    light_rain_label3 = Label(image=light_rain3)
    thunder_with_rain_label3 = Label(image=thunder_with_rain3)
    thunder_without_rain_label3 = Label(image=thunder_without_rain3)
    snowy_label3 = Label(image=snowy3)
    windy_label3 = Label(image=windy3)
    foggy_label3 = Label(image=foggy3)
    weather_time3 = box3["dt_txt"]
    weather_day3 = str(weather_time3).split(" ")[0].split("-")[1] + "/" + str(weather_time3).split(" ")[0].split("-")[2]
    weather_hour_raw3 = str(weather_time3).split(" ")[1].split(":")[0]
    if int(weather_hour_raw3) == 0: weather_hour3 = "12 AM"
    elif int(weather_hour_raw3) < 12: weather_hour3 = str(int(weather_hour_raw3)) + " AM"
    elif int(weather_hour_raw3) == 12: weather_hour3 = "12 PM"
    elif int(weather_hour_raw3) > 12: weather_hour3 = str(int(weather_hour_raw3) - 12) + " PM"
    weather_month3 = str(weather_time3).split(" ")[0].split("-")[1]
    time_of_day3 = find_day_or_night(weather_month3, weather_hour_raw3)
    if box3["weather"][0]["main"] == "Thunderstorm":
        if box3["weather"][0]["description"] == "thunderstorm with light rain": thunder_without_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "thunderstorm with rain": thunder_with_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "thunderstorm with heavy rain": thunder_with_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "light thunderstorm": thunder_without_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "thunderstorm": thunder_with_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "heavy thunderstorm": thunder_with_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "ragged thunderstorm": thunder_with_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "thunderstorm with light drizzle": thunder_without_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "thunderstorm with drizzle": thunder_without_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        else: thunder_with_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Rain": heavy_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Drizzle": light_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Clear":
        if time_of_day3 == 'day': sunny_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        else: clear_night_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Snow": snowy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Clouds":
        if box3["weather"][0]["description"] == "few clouds":
            if time_of_day3 == 'day': partly_cloudy_day_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
            else: partly_cloudy_night_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "scattered clouds":
            if time_of_day3 == 'day': partly_cloudy_day_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
            else: partly_cloudy_night_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        elif box3["weather"][0]["description"] == "broken clouds": cloudy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
        else: cloudy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Mist": foggy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Smoke": windy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Haze": foggy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Dust": windy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Ash": windy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    elif box3["weather"][0]["main"] == "Squall": heavy_rain_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    else: windy_label3.place(x=517.5, y=695, relwidth=0.05, relheight=0.1)
    def open_weather_details3(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Weather_Details_HTML_Page.html", shell = True)	
    weather_details_button3 = Button(button_master, text=weather_hour3 + "    " + weather_day3, background = 'white', command=open_weather_details3)
    weather_details_button3.config(font=('lato', 16, 'bold'))
    weather_details_button3.config(height = 2, width = 10)
    weather_details_button3.configure(foreground = 'red')
    weather_details_button3.place(x = 570, y = 645, anchor="center")
    canvas.tag_raise(weather_details_button3)
    temperature3 = int(((box3["main"]["temp"]) * 9/5) - 459.67)
    temperature_label3 = Label(text=str(temperature3)+degrees_sign)
    temperature_label3.place(x=570, y=848, anchor="center")
    temperature_label3.config(font=temperature_font, foreground='red', bg='white')
    weather_description3 = box3["weather"][0]["main"]
    weather_description_label3 = Label(text=weather_description3)
    weather_description_label3.place(x=570, y=808, anchor="center")
    weather_description_label3.config(font=weather_description_font, foreground='red', bg='white')



def check_weather():
    #http://api.openweathermap.org/data/2.5/forecast?appid=665c0a4c70ee4aecec2fd415645cc9fc&q=new%20york
    #api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=665c0a4c70ee4aecec2fd415645cc9fc&q='
    api_address = 'http://api.openweathermap.org/data/2.5/forecast?appid=665c0a4c70ee4aecec2fd415645cc9fc&q='
    city = "new york"
    url = api_address + city
    json_data = requests.get(url).json()
    box1 = json_data["list"][0]
    box2 = json_data["list"][1]
    box3 = json_data["list"][2]
    print(int(((box1["main"]["temp"]) * 9/5) - 459.67))
    print(box1["weather"][0]["main"])
    print(box1["weather"][0]["description"])
    print(box1["dt_txt"])
    print(int(((box2["main"]["temp"]) * 9/5) - 459.67))
    print(box2["weather"][0]["main"])
    print(box2["weather"][0]["description"])
    print(box2["dt_txt"])
    print(int(((box3["main"]["temp"]) * 9/5) - 459.67))
    print(box3["weather"][0]["main"])
    print(box3["weather"][0]["description"])
    print(box3["dt_txt"])
    print("\n")
    
    change_weather_picture()
    
    time_clock.after(600000, check_weather) #900000 is 15 minutes and is 600000 10 minutes

check_weather()


with open('day.csv') as csv_file:
    todays_date = strftime('%m/%d/%y')
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if todays_date == row[1]:
            day = row[0]
            if day == '1': day_color = '#D02A2F' # RED
            elif day == '2': day_color = '#E48D1A' #ORANGE
            elif day == '3': day_color = '#8F4E6A' #PURPLE
            elif day == '4': day_color = '#A6A937' #GREEN
            elif day == '5': day_color = '#444f69' #BLUE
            elif day == '6': day_color = '#00a5a8' #TEAL
            else: day_color = 'black'
            day_number = str(day)
            day_number_frame1 = Frame(button_master, highlightbackground=day_color, highlightthickness=20, width=250, height=300, bd= 0, bg="white")
            day_number_frame1.place(x = 690, y = 595)
            if day > 0 and day < 7:
                day_number_frame2 = Frame(button_master, highlightbackground=day_color, highlightthickness=20, width=250, height=100, bd= 0, bg="white")
                day_number_frame2.place(x = 690, y = 595)
                number_text = Label(button_master, text=day_number, bg="white")
                number_text.config(font=('lato', 110, 'bold'), foreground=day_color)
                number_text.place(x = 765, y = 695)
                day_number_text = Label(button_master, text="Today is day ...", bg="white")
                day_number_text.config(font=('lato', 23, 'bold'), foreground=day_color)
                day_number_text.place(x = 710, y = 622.5)
            else:
                no_school_text1 = Label(button_master, text="NO", bg="white")
                no_school_text1.config(font=('lato', 37, 'bold'), foreground='black')
                no_school_text1.place(x = 775, y = 675)
                no_school_text2 = Label(button_master, text="SCHOOL", bg="white")
                no_school_text2.config(font=('lato', 37, 'bold'), foreground='black')
                no_school_text2.place(x = 710, y = 755)
    
button_master.configure(bg='white')

def tick(): #https://docs.python.org/2/library/datetime.
    current_time = time.strftime('%I:%M:%S %p')
    current_day = time.strftime('%m/%d/%y')
    time_clock.config(text = current_time)
    day_clock.config(text = current_day)
    check_day()
    time_clock.after(200, tick)

def check_day():
    now_time = time.time()
    #if now_time - last_day_time_checked > 3600000:
    #    check_day()

def restart_slideshow_timer():
    print("timer started")
    timer = threading.Timer(600, play_slideshow) #10 minutes
    timer.start()
def play_slideshow():
    os.system('python Slideshow_Final.py')
    timer.cancel()
    restart_slideshow_timer()
#timer = threading.Timer(600, play_slideshow) #10 minutes

def refresh():
    #current_time = time.strftime('%I:%M:%S %p')
    #current_day = time.strftime('%m/%d/%y')
    #time_clock.config(text = current_time)
    #day_clock.config(text = current_day)
    #check_day()
    #Tk.update()
    button_master.update()
    print("refreshed")
    time_clock.after(1260000, refresh) #21 minutes


    
def open_Brearley_Website(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Brearley_Website_HTML_Page.html", shell = True)
homepage_button = Button(button_master, text="Go to Brearley Homepage", background = 'red', command=open_Brearley_Website)
homepage_button.config(font=button_font)
homepage_button.config(height = 3, width = 50)
homepage_button.configure(foreground = 'white')
homepage_button.place(x = 966, y = 40)

def open_Brearley_Calendar(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/Brearley_Calendar_HTML_Page.html", shell = True)	
calendar_button = Button(button_master, text="Go to Brearley Calendar", background = 'red', command=open_Brearley_Calendar)
calendar_button.config(font=button_font)
calendar_button.config(height = 3, width = 50)
calendar_button.configure(foreground = 'white')
calendar_button.place(x = 966, y = 225)

def open_Photo_Booth():
    with picamera.PiCamera() as camera:

        camera.start_preview()
        img = Image.open('/home/pi/Desktop/3.png')

        pad = Image.new('RGBA', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ))

        pad.paste(img, (0, 0))

        o = camera.add_overlay(pad.tobytes(), size=img.size)
        o.alpha = 255
        o.layer = 3

        sleep(1)
    
        for o in camera.overlays:
            camera.remove_overlay(o)
            
        img = Image.open('/home/pi/Desktop/2.png')

        pad = Image.new('RGBA', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ))

        pad.paste(img, (0, 0))

        o = camera.add_overlay(pad.tobytes(), size=img.size)
        o.alpha = 255
        o.layer = 3

        sleep(1)
    
        for o in camera.overlays:
            camera.remove_overlay(o)
        
        img = Image.open('/home/pi/Desktop/1.png')

        pad = Image.new('RGBA', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ))

        pad.paste(img, (0, 0))

        o = camera.add_overlay(pad.tobytes(), size=img.size)
        o.alpha = 255
        o.layer = 3

        sleep(1)
        for o in camera.overlays:
            camera.remove_overlay(o)
        
        current_time = strftime("%Y-%m-%d-%H-%S",gmtime())
        image_file = str('/home/pi/Desktop/Photobooth/610_lobby_phototbooth-'+ str(current_time) +'.jpg')
        camera.capture(image_file)
        sleep(1)
        camera.stop_preview()
Photo_Booth_button = Button(button_master, text="Photo Booth", background = 'red', command=open_Photo_Booth)
Photo_Booth_button.config(font=button_font)
Photo_Booth_button.config(height = 3, width = 50)
Photo_Booth_button.configure(foreground = 'white')
Photo_Booth_button.place(x = 966, y = 410)

def open_language_trivia_questions(): os.system('python Language_Menu.py')
language_trivia_button = Button(button_master, text="Language Trivia Questions", background = 'red', command=open_language_trivia_questions)
language_trivia_button.config(font=button_font)
language_trivia_button.config(height = 3, width = 50)
language_trivia_button.configure(foreground = 'white')
language_trivia_button.place(x = 966, y = 595)

def open_national_days(): subprocess.call("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk file:///home/pi/Desktop/National_Days_HTML_Page.html", shell = True)
national_day_button = Button(button_master, text="Today's National Day", background = 'red', command=open_national_days)
national_day_button.config(font=button_font)
national_day_button.config(height = 3, width = 50)
national_day_button.configure(foreground = 'white')
national_day_button.place(x = 966, y = 780)


refresh()
#restart_slideshow_timer()
change_weather_picture()
tick()
button_master.mainloop()