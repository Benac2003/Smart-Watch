"""
Main/core program that runs in the background:
Runs kivy gui and time
""" 
#data
from Main_DateTime import timeUpdate
from StoringVariables import Data_get, main

#threading
from multiprocessing import Value
from threading import Thread

 #Threading
def loopInc(cond, hourclock):
    while(not cond.value):
        ticks, second, minute, hour, pm = timeUpdate(ticks, hourclock, minute, second, hour, pm)
        main(ticks, minute, second, hour, hourclock, pm, day, month, year)

    return

#main
if __name__ == '__main__':
    #threading
    cond = Value("b", False)
    hourclock = Value("b", True)
    p = Thread(target=loopInc, args=(cond, hourclock.value))
    p.start()
    p.join()