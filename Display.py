"""
Does the display and user interaction
"""

# modules
import psutil
#battery
def Battery_Status(app):
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    Battery_stats = str(percent),"%"
    if plugged == False:
        print(percent)
        if 70 < percent <=100:
            plugged = "image/100charge.png"
        elif 50 < percent <=70:
            plugged = "image/70charge.png"
        elif 30 < percent <=60:
            plugged = "image/50charge.png"
        elif 20 < percent <=30:
            plugged = "image/30charge.png"
        elif 10 < percent <=20:
            plugged = "image/20charge.png"
        elif percent <=10:
            plugged = "image/0charge.png"
    else: plugged = "image/charged.png"
    try:
        return Battery_stats, plugged
    except:
        Battery_error = "No Battery_stats"
        print(Battery_error)

def New_Battery_Status(app):
    Battery_stats, plugged = Battery_Status(app)
    Battery_Percent = Text(app, text=Battery_stats, size=60, grid=[1,0], align="top",color="#04CCF0", bg="#262626")
    Battery_Icon = Picture(app, image=plugged, grid=[1,0], align="right")
    Battery_Icon.height = 70
    Battery_Icon.width = 140
    return Battery_Icon, Battery_Percent

def Update_Battery_Status(app, Battery_Percent, Battery_Icon):
    Battery_stats, plugged = Battery_Status(app)
    Battery_Percent.value = Battery_stats
    Battery_Icon.image = plugged
    return Battery_Percent, Battery_Icon



#Time Display
def Timevalue(day, month, year, hour, minute, second, pm):
    #update current_date and current_time
    current_date = "%02d/%02d/%04d" % (day, month, year)
    current_time = "%02d : %02d : %02d" % (hour, minute, second)
    return current_date, current_time


def TimeDisplay(day, month, year, hour, minute, second, pm):
    #time and date display
    app = App(title="Smart Watch", layout="grid", bg="black", height="720", width="1080")
    current_date, current_time = Timevalue(day, month, year, hour.value, minute.value, second.value, pm)
    time = Text(app, current_time, size=140, font="Arial Black",color="#04CCF0", grid=[0, 0], align="top", bg=(0, 0, 0,))
    date = Text(app, current_date, size=140, font="Arial Black",color="#04CCF0", grid=[0, 1], align="bottom", bg=(0, 0, 0))
    pmgui = Text(app, "pm", size=70, font="Arial Black", color="#04CCF0",grid=[3, 0], align="right", bg=(0, 0, 0))
    Slideopen_loading = Picture(app, image="image/Loading.gif",grid=[0, 3], visible=True, enabled=True, align="bottom")
    pmgui.repeat(1, lambda: updatepm(pm.value, pmgui))
    time.repeat(1, lambda: Updategui(hour.value, second.value, minute.value, time, day, month, year, date))
    Slideopen_loading.when_mouse_dragged = destroy_app
    app.display()


def destroy_app(app):
    #destroy app and calls openapp
    app.widget.master.destroy()
    openapp()
 
def update_Newtime(time,pm, pmgui, Battery_Percent, Battery_Icon):
            ticks, hour, minute, second, day, month, year, pm = Data_get()
            updatepm(pm, pmgui)
            time.value = "%02d : %02d : %02d" % (hour, minute, second)
            Battery_Percent, Battery_Icon = Update_Battery_Status(openapp, Battery_Percent, Battery_Icon)

def openapp():
    #new gui and time is created
    openapp = App(title="Openapp", layout="grid", width=1080, height=720, bg="#262626")
    ticks, hour, minute, second, day, month, year, pm = Data_get()
    current_date, current_time = Timevalue(day, month, year, hour, minute, second, pm)
    backgroundLeft = Picture(openapp, image="image/Moon_Colour_Shine_Left.jpg", align='bottom', grid=[0,1])
    backgroundLeft.height = 630
    backgroundLeft.width = 540    
    backgroundRight = Picture(openapp, image="image/Moon_Colour_Shine_Right.jpg", align='bottom', grid=[1,1])
    backgroundRight.height = 630
    backgroundRight.width = 540
    time = Text(openapp, current_time, size=60, font="Arial Black", color="#04CCF0", grid=[0, 0], align="top", bg="#262626")
    pmgui = Text(openapp, "pm", size=40, font="Arial Black", color="#04CCF0",grid=[0, 0], align="right", bg="#262626")
    Battery_Percent, Battery_Icon = New_Battery_Status(openapp)
    time.repeat(1, lambda:update_Newtime(time, pm, pmgui, Battery_Percent, Battery_Icon))
    
    
    
