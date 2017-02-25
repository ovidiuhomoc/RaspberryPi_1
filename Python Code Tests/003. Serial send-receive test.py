import serial
import threading
from gpiozero import LED,Button
import time,datetime

def read_serial(port):
    print ("Started serial listening")
    while True:
        rv=""
        flag=0

        while flag==0:
            ch=port.read()
            rv+=ch
            if (ch=='\r') or (ch=='\n'):
                print ("Got from serial below string \n%s"%(cv.decode('utf-8')))
                flag=1

def write_serial(i):
    try:
        ser.write("s-a apasat butonul {} la ora {}".format(i.pin.number,datetime.datetime.now()))
    except:
        pass

In1=Button(18)
flag=0

ser=serial.Serial("/dev/ttyAMA0",baudrate=115200,timeout=0)
try:
    ser.open()
    flag =1
except Exception as inst:
    print ("Nu s-a putut deschide portul iar exceptia este :{}".format(inst))           # __str__ allows args to be printed directly

if flag:
    threading (read_serial,[ser]).start()
    In1.when_pressed=write_serial
