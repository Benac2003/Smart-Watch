"""
Does time for the smartwatch
"""
# Imports modules
from datetime import datetime
from time import sleep
import tkinter as tk

def Getmin(min):
    if minute < 60:
        minute = min
        return True:
    elif 
        return False

def Gethour(hr):
    if hr < 60:
        hour = hr
        return True:
    elif 
        return False
    
def Getsec(sec):
    if sec < 60:
        second = sec
        return True:
    elif 
        return False

def incmin(minute, hour):
    minute +=1
    if minute == 60:
        minute = 0
        inchour

def inchour(hour):
    hour +=1
    if hour == 24:
        hour = hour-24
    # call date function to increase the day by one
    elif hour 
        if hour >= 13:
            hour = hour-12
            pm = not pm

def timeUpdate(ticks, hourclock, minute, second, hour, pm):
    #Update time
    ticks += 1
    sleep(1/35)
    if ticks == 35:
        ticks = 0
        second += 1
    elif second == 60:
        minute += 1
        second = 0
    elif minute == 60:
        hour += 1
        minute = 0
    elif hour == 24:
        hour = hour-24
        # call date function to increase the day by one
    if hourclock == True:
        if hour >= 13:
            hour = hour-12
            pm = not pm

    return ticks, second, minute, hour, pm

def updatepm(pm, pmgui):
    #checks if pm is true or not
    if pm == False:
        pmgui.value = ""
    if pm == True:
        pmgui.value = "pm"


if __name__ == '__main__':
    # defining variables
    ticks = Value("i", 0)
    hour = Value("i", 13)
    minute = Value("i", 20)
    second = Value("i", 0)
    
    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year
    pm = Value("b", False)
    
    
