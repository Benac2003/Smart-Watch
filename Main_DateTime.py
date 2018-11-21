"""
Does time for the smartwatch
"""
# Imports modules
from datetime import datetime
from time import sleep
import tkinter as tk
def getpm(at):
       if at == True:
          pm = at
          return True, at
       else:
           return False

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

def incsec(second,minute,hour):
    sleep(1)
    second +=1
    if second == 60:
        second = 0
        incmin
    return second


def incmin(minute,hour):
    minute +=1
    if minute == 60:
        minute = 0
        inchour
    return minute


def inchour(hour, pm):
    hour +=1
    if hour == 24:
        hour = hour-24
    # call date function to increase the day by one
    else:
        if hour >= 13:
            hour = hour-12
            pm = not pm


def updatepm(pm, pmgui):
    #checks if pm is true or not
    if pm == False:
        pmgui.value = ""
    else:
        pmgui.value = "pm"


if __name__ == '__main__':
    # defining variables
    second = 49
    minute = 49
    hour = 49
    while(True):
        if (Getsec(second) and Getmin(minute) and Gethour(hour)):
                incsec(second,minute,hour)
                print(minute)

 
    
    
