from microbit import *
import radio
import random
radio.on()
def on_gesture_tilt_left():
    a=[]
    a.append(random.randint(0,10))
    a.append(random.randint(0,10))
    a.append(random.randint(0,10))
    radio.config(channel=0)
    radio.send(a[0])
    radio.config(channel=1)
    radio.send(a[1])
    radio.config(channel=2)
    radio.send(a[2])
