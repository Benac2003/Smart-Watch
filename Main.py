"""
Main/core program that runs in the background:
Runs kivy gui and time
""" 
#data
from Datetime import incsec, inchour, incmin
from StoringVariables import Data_get, main

#threading
from multiprocessing import Value
from threading import Thread

 #Threading
def loopInc(cond, hourclock):
    while(not cond.value):
        second = incsec(second)
        minute =  incmin(minute)
        hour, pm = inchour(hour,pm)
    return

#main
if __name__ == '__main__':
    #threading
    cond = Value("b", False)
    hourclock = Value("b", True)
    p = Thread(target=loopInc, args=(cond, hourclock.value))
    p.start()
    p.join()