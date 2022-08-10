from tkinter import *
from tkinter.ttk import *

from time import strftime

main = Tk()

main.title("The Digital Clock")

def clock():
    hour = strftime('%H')
    if hour == '00' or hour == '0' or hour == None:
        hour = "12"
        
        
    tick = strftime(':%M:%S %p')
    
    clock_label .config(text = hour + tick)
    
    clock_label .after(1000, clock)
    
clock_label = Label(main, font = ('sans', 80), background = 'black', foreground = 'white')

clock_label.pack(anchor= 'center')

clock()
mainloop()