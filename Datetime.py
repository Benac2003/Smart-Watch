."""
Does time for the smartwatch
"""
# Imports modules
from datetime import datetime
from time import sleep
import tkinter as tk
from StoringVariable import Data_get
#check variables
def Getmin(min):
    if min < 60:
        minute = min
        return True
    else:
        return False

def Gethour(hr):
    if hr < 60:
        hour = hr
        return True
    else:
        return False
    
def Getsec(sec):
    if sec < 60:
        second = sec
        return True
    else:
        return False
#increments variables
def incsec(second):
    sleep(1)
    second +=1
    if second == 60:
        second = 0
        return second
    return second

def incmin(minute):
    minute +=1
    if minute == 60:
        minute = 0
        return minute
    return minute

def inchour(hour, pm):
    hour +=1
    if hour == 24:
        hour = hour-24
        return hour, pm
    # call date function to increase the day by one
    else:
        if hour >= 13:
            hour = hour-12
            pm = not pm
            return hour, pm
    return hour, pm


def updatepm(pm, pmgui):
    if pm == False:
        pmgui.value = ""
    else:
        pmgui.value = "pm"


if __name__ == '__main__':
    second, hour, minute = Data_get('time')
    pm = True
    while(True):
        second = incsec(second)
        minute =  incmin(minute)
        hour, pm = inchour(hour,pm)
        print(minute)

 
    
    
