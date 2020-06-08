from tkinter import *
import tkinter.font
from smbus import SMBus
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

# Set up bus
address = 0x40
bus = SMBus(1)

## GUI DEFINITIONS ##
win = Tk()
win.title('Smart Chicken Coop')
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


## Event Functions
def flock():
    chickens = key.get()
    bus.write_byte(address, chickens)
    print(chickens)

def sensingTime():
    print('Currently unable to set time')

def data():
    print('Currently unable to show data')

def close():
    win.destroy()

### WIDGETS ###
setFlock = Button(win, text = 'Enter the number of chickens in your flock', font = myFont, command = flock, bg = 'bisque2', height = 1)
setFlock.grid(row=0,column=0)
key = Entry(win, font=myFont, width=12)
key.grid(row=0,column=2)
setTime = Button(win, text='Set time to begin sensing', font = myFont, command = sensingTime, bg = 'bisque2', height=1)
setTime.grid(row=3,column=0, sticky=E)
viewData = Button(win, text='View data', font = myFont, command = data, bg = 'bisque2', height=1)
viewData.grid(row=5,column=0, sticky=E)
exitButton = Button(win, text='Exit', font = myFont, command= close , bg = 'red', height=1, width=6)
exitButton.grid(row=7,column=0, sticky=E)


win.protocol("WM_DELETE_WINDOW", close) 
win.mainloop()