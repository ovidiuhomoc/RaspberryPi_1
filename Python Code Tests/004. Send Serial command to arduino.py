import serial
import threading
from gpiozero import LED,Button
import time,datetime
import codecs

def read_serial(port):
    print ("Serial ascult")
    while True:
        rv=""
        flag=0

        while flag==0:
            ch=port.read()
            if (ch<>'\r') and (ch<>'\n'):
                rv+=ch
            
            if (ch=='\r') or (ch=='\n'):
                print ("Serial recept:{}\n".format(rv))
                flag=1

def button_press():
    threading.Thread(target=write_serial,args=[1]).start()
    threading.Timer(2,write_serial,[2]).start()

def write_serial(i):
    
    adr_exp=10
    adr_dest=1
    elemente=15
    final=5

    print ("Serial trimis:")
    
    try:
        ser.write("{}|{}|{}|{}|{}\n\r".format(adr_exp,adr_dest,i,elemente,final))
        print ("{}|{}|{}|{}|{}".format(adr_exp,adr_dest,i,elemente,final))
    except Exception as inst:
        print ("nu s-a trecut de try iar exceptia este: {}".format(inst))    
        pass
    
In1=Button(18)
portSerial=0

try:
    ser=serial.Serial(
        port="/dev/ttyS0",
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        rtscts=0,
        xonxoff=0,
        dsrdtr=0,
        timeout=None
    )
    
    if (ser.isOpen()):
        print("Serial deschis")
        portSerial =1
    else:
        print("Serial !deschis")
except Exception as inst:
    print ("Eroare deschidere serial:{}".format(inst))           # __str__ allows args to be printed directly

if portSerial:
    t=threading.Thread(target=read_serial,args=[ser])
    t.start()
    In1.when_pressed=button_press