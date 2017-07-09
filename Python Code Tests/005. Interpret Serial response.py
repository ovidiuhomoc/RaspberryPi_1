import serial
import threading
from gpiozero import LED,Button
import time,datetime
import codecs
import string
from string import *

portSerial=0
serialFlag=0

def decode_string(text):
    counter=0
    sep="|"
    sep1=text.find(sep)
    inByte=[]
    
    if (sep1!=-1):
        y=len(text)
        x=text[:sep1]
        counter=counter+1
        inByte.append(int(x))

        lastIndex=text.rfind(sep)

        while sep1!=lastIndex:
            x=text[sep1+1:text.find(sep,sep1+1)]
            counter=counter+1
            inByte.append(int(x))
            sep1=text.find(sep,sep1+1)

        x=text[sep1+1]
        counter=counter+1
        inByte.append(int(x))

        for i in inByte:
            print ("\{}/".format(i))
        print("*{}*".format(counter))

def read_serial(port):
    print ("Serial ascult")
    global serialFlag
    oldSerialFlag=serialFlag
    
    while True:
        rv=""
        flag=0
        if(oldSerialFlag!=serialFlag):
            print("serialFlag={}".format(serialFlag))
            oldSerialFlag=serialFlag
            time.sleep(1)

        
        while (flag==0)&(serialFlag==0):            
            ch=port.read()
            if (ch<>'\r') and (ch<>'\n'):
                rv+=ch
            
            if (ch=='\r') or (ch=='\n'):
                print ("Serial recept:{}\n".format(rv))
                #decode_string(rv)
                flag=1

def button_press():
    threading.Thread(target=write_serial,args=[1]).start()
    threading.Timer(2,write_serial,[2]).start()

def write_serial(i):

    global serialFlag
    
    adr_exp=10
    adr_dest=1
    elemente=15
    final=5

    try:
        serialFlag=1
        print(serialFlag)
        print("-------------------------------------")
        ser.write("{}|{}|{}|{}|{}\n\r".format(adr_exp,adr_dest,i,elemente,final))
        print ("Serial trimis:{}|{}|{}|{}|{}\n".format(adr_exp,adr_dest,i,elemente,final))
        serialFlag=0
        print(serialFlag)
    except Exception as inst:
        print ("Eroare transmisiune seriala: {}".format(inst))
        serialFlag=1
        pass
    
In1=Button(18)

try:
    global ser
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
