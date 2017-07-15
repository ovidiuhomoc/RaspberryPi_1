def init(d,w,h,dev):

    # d 32(+1) dispozitive pe BUS, max 6(+1) in/out, max 8(+1) atribute
    #dev = [[[0 for x in range(w)] for y in range(h)] for z in range(h)]

    for z in range(0,d):
        device=[]
        device.append("")       #dev[z][0]      not used
        device.append("")       #dev[z][1]      device label
        device.append("")       #dev[z][2]      device descriptor
        device.append(0)        #dev[z][3]      device type
        device.append(0)        #dev[z][4]      device address
        device.append(0)        #dev[z][5]      device serial number
    
        inpt=[]
        for j in range(0,w):
            inpt.append(0)
        device.append(inpt)       #dev[z][6][j]   in status
    
        out=[]
        for j in range(0,w):
            out.append(0)
        device.append(out)      #dev[z][7][j]   out status

        pendOut=[]
        for j in range(0,w):
            pendOut.append(0)
        device.append(pendOut)  #dev[z][8][j]   pneding out change

        dev.append(device)
    return dev
