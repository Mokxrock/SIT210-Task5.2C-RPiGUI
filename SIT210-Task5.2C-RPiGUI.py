#Task 5.2
from tkinter import * # Import functions from tkinter
import tkinter.font # import fonts 
from gpiozero import LED # import function from specific roles just like GPIO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# LED function 
green = LED(18) # Green LED connect to PIN 18
yellow = LED(23) # Yellow LED connect to PIN 23
red = LED(24) # Red LED connect to PIN 24

#GUI DEF
win = Tk() # Window set as Tk(), Tk() create a object that allow us to build the GUI in
win.title("PARTY TIME") # set Title Of the Window 
myFont = (tkinter.font.Font(family = 'Helvetica', size=15, weight="bold" )) #set fonts 



# Event Function
# Turn On Red LED 
def redLED(): 
    if red.is_lit:
        red.off()
        redButton["text"] = "Red"
        
    else:
        red.on()
        green.off()
        yellow.off()
        #redButton["text"] = "Red Off"
        
# Turn On Yellow LED 
def yellowLED(): 
    if yellow.is_lit:
        yellow.off()
        yellowButton["text"] = "Yellow"
        
    else:
        yellow.on()
        red.off()
        green.off()
        #greenButton["text"] = "Yellow Off"
       
# Turn On Green LED 
def greenLED(): 
    if green.is_lit:
        green.off()
        greenButton["text"] = "Green"
        
    else:
        green.on()
        red.off()
        yellow.off()
        #greenButton["text"] = "Green Off"
       
def bye():
    GPIO.cleanup()
    win.destroy()

# GREEN BUTTON DESIGN
greenButton = Button(win, text='GREEN', font=myFont, command= greenLED, bg= 'green', height = 1, width=24)
greenButton.grid(row=0, column=1)
                      
# YELLOW BUTTON DESIGN
yellowButton = Button(win, text='YELLOW', font=myFont, command=yellowLED , bg= 'yellow', height = 1, width=24)
yellowButton.grid(row=1, column=1)

# RED BUTTON DESIGN
redButton = Button(win, text='RED', font=myFont, command= redLED, bg= 'red', height = 1, width=24)
redButton.grid(row=2, column=1)

# EXIT BUTTON DESIGN
endLED = Button(win, text='Bye Bye', font=myFont, command= bye, bg= 'white', height = 1, width=6)
endLED.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", bye) #EXIT CLEANLY
win.mainloop() #Loop forever
