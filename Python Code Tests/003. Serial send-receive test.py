import serial
import threading
from gpiozero import LED,Button
import time,datetime
import codecs

def read_serial(port):
    print ("Started serial listening")
    while True:
        rv=""
        flag=0

        while flag==0:
            ch=port.read()
            if (ch<>'\r') and (ch<>'\n'):
                rv+=ch
            
            if (ch=='\r') or (ch=='\n'):
                print ("Got from serial below string \n{}".format(rv))
                flag=1

def write_serial(i):
    try:
        ser.write("s-a apasat butonul {} la ora {}\n\r".format(i.pin.number,datetime.datetime.now()))
        print ("__s-a apasat butonul {} la ora {}".format(i.pin.number,datetime.datetime.now()))
    except:
        pass

In1=Button(18)
flag=0

try:
    ser=serial.Serial(
        port="/dev/ttyS0",
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE
    )
    
    if (ser.isOpen()):
        print("Portul este deschis")
    else:
        print("Portul nu este deschis")
    flag =1
except Exception as inst:
    print ("Nu s-a putut deschide portul iar exceptia este :{}".format(inst))           # __str__ allows args to be printed directly

if flag:
    t=threading.Thread(target=read_serial,args=[ser])
    t.start()
    In1.when_pressed=write_serial
