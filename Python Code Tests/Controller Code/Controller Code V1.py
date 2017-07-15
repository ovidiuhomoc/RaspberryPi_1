import serial,time,datetime,string,threading
from gpiozero import LED,Button
#import codecs

#-------------------------------------------
#import extra programmed modules
#-------------------------------------------

import rs485
import opsys
import settings

#-------------------------------------------
#definition / initialization of global vars
#-------------------------------------------

portSerial=0
d =33 
w =7
h =9
dev=[]

dev=settings.init(d,w,h,dev)

#-------------------------------------------
#main functions
#-------------------------------------------

dev=opsys.addDev(dev,1,"Controller #1","Camera tehnica IT etaj 2",641,1,100,[0,1,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,1,0,0,0])
opsys.listDev(5,w,h,dev,0)

"""
dev=opsys.setDevAttr(dev,1,2,"Camera tehnica IT parter")
opsys.listDev(2,w,h,dev,0)

dev=opsys.setDevAttrId(dev,1,7,2,0)
opsys.listDev(2,w,h,dev,0)
"""
