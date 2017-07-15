def listDev(d,w,h,dev,k):
    for z in range(0,d):
        print ("\ndispozitiv {}".format(z))
        for i in range(0,h):
            print ("\n             parametru {}".format(i)),
            if i<6:
                print ("<{}>".format(dev[z][i])),
            else:
                for j in range(0,w):
                    print ("<{}>".format(dev[z][i][j])),
        if k==1:
            var=raw_input("Continue?")

def addDev(dev,devId,label,descr,ver,addr,ser,inp,out,pendOut):
    dev[devId][1]=label               #label of device
    dev[devId][2]=descr               #device description
    dev[devId][3]=ver                 #device version ex:I/O 6/4 -> 64 versiunea 1
    dev[devId][4]=addr                #device address
    dev[devId][5]=ser                 #device serial number
    dev[devId][6]=inp                 #device input state
    dev[devId][7]=out                 #device output state
    dev[devId][8]=pendOut             #device pending output state
    return dev

def setDevAttr(dev,devId,attr,val):
    if attr<6:
        dev[devId][attr]=val
    return dev

def setDevAttrId(dev,devId,attr,attrId,val):
    if attr>5:
        dev[devId][attr][attrId]=val
    return dev
