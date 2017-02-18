from gpiozero import LED, Button
import threading
import time

In1=Button(18)
In2=Button(23)

Out1=LED(24)
Out2=LED(25)

def button_press(i):
    print ("Button %d was pressed"%(i))
    if i==1:
        threading.Timer(1,run_leds,args=[1,i],kwargs=None)
        threading.Timer(2,run_leds,args=[2,i],kwargs=None)
    elif i==2:
        threading.Timer(2,run_leds,args=[1,i],kwargs=None)
        threading.Timer(1,run_leds,args=[2,i],kwargs=None)
    else:
        print("No actions taken")

def run_leds(mode,led):
    if mode==1:
        if led==1:
            Out1=led.on
            time.sleep(3)
            Out1=led.off
        else:
            Out2=led.on
            time.sleep(3)
            Out2=led.off
    else:
        if led==1:
            Out1=led.on
            time.sleep(1)
            Out1=led.off
            time.sleep(1)
            Out1=led.on
            time.sleep(1)
            Out1=led.off
        else:
            Out2=led.on
            time.sleep(1)
            Out2=led.off
            time.sleep(1)
            Out2=led.on
            time.sleep(1)
            Out2=led.off

In1.when_pressed=button_press(1)
In2.when_released=button_press(2)
