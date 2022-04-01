from microbit import *
import radio
radio.config(channel=0)

def cycle(a):


while True:
    transmit=radio.recive()
    if transmit!="None" and len(transmit)!=0:
        cycle(transmit)
