from gpiozero import LED,Button,Pin

In = range(0,27)

for i in range (1,27):
    In[i]=Button(i,pull_up=True)

def button_press(i):
    print ("Button %d"%(i.pin.number))

for i in range (1,27):
    In[i].when_pressed=button_press
