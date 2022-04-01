from microbit import *
import radio
import random
radio.on()
def on_gesture_tilt_left():
    a=[]
    a.append(random.randint(0,9))
    a.append(random.randint(0,9))
    if a[0]==a[1]:
        a[1]=random.randint(0,9)
    a.append(random.randint(0,9))
    if a[0]==a[1]==a[2]:
        a[2]=random.randint(0,9)
    radio.config(channel=0)
    radio.send(a[0])
    radio.config(channel=1)
    radio.send(a[1])
    radio.config(channel=2)
    radio.send(a[2])
