from gpiozero import LED, Button
import threading
import time

In1=Button(18)
In2=Button(23)

Out1=LED(24)
Out2=LED(25)

def button_press(i):

    pin=i.pin.number
    print ("Button %d was pressed"%(pin))
    if pin==18:
        print ("Process thread 18")
        threading.Timer(1,run_leds,[1,1]).start()
        threading.Timer(2,run_leds,[1,1]).start()
        
    elif pin==23:
        print ("Process thread 23")
        threading.Timer(2,run_leds,[1,1]).start()
        threading.Timer(1,run_leds,[2,2]).start()
    else:
        print("No actions taken")

def run_leds(mode,led):

    print("Thread cu mode = %d si led-ul %d/n"%(mode,led))

    if mode==1:
        if led==1:
            Out1.on()
            time.sleep(3)
            Out1.off()
        else:
            Out2.on()
            time.sleep(3)
            Out2.off()
    else:
        if led==1:
            Out1.on()
            time.sleep(1)
            Out1.off()
            time.sleep(1)
            Out1.on()
            time.sleep(1)
            Out1.off()
        else:
            Out2.on()
            time.sleep(1)
            Out2.off()
            time.sleep(1)
            Out2.on()
            time.sleep(1)
            Out2.off()

In1.when_pressed=button_press
In2.when_released=button_press
