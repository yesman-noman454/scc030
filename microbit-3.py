from microbit import *
import radio
import random
import utime
radio.on()
radioChannel=1
radio.config(group=radioChannel)
a=True
while a:
    transmit=radio.receive()
    if transmit=='1':
        a=False
        display.show(Image.HEART)

b=random.randint(0,9)
radio.send(str(b))

radio.config(group=10)
a=True
while a:
    transmitTwo=radio.receive()
    if transmitTwo=='1'or transmitTwo=='2' or transmitTwo=='3':
        a=False
        n=1


zero=Image("90909:"
    "09090:"
    "90909:"
    "09090:"
    "90909")

one=Image("00000:"
    "09090:"
    "09990:"
    "00900:"
    "00000")

two=Image("00900:"
    "09090:"
    "90009:"
    "09090:"
    "00900")

three=Image("00000:"
    "09990:"
    "09090:"
    "09990:"
    "0000")

four=Image("00000:"
    "99999:"
    "00000:"
    "99999:"
    "00000")

five=Image("09009:"
    "90090:"
    "00900:"
    "09009:"
    "90090")

six=Image("09090:"
    "09090:"
    "09090:"
    "09090:"
    "09090")

seven=Image("09090:"
    "09090:"
    "90009:"
    "09990:"
    "00000")

eight=Image("99909:"
    "90009:"
    "90909:"
    "90909:"
    "90909")

nine=Image("90909:"
    "09990:"
    "99999:"
    "09990:"
    "90909")




symbols=[zero,one,two,three,four,five,six,seven,eight,nine]
def cycle(c,symbols):
    for i in range(9):
        display.show(symbols,delay=100)
    display.show(symbols[c])

if n==1:
    cycle(b,symbols)

utime.sleep(4)

if transmitTwo=='2':
    display.scroll('win')
    utime.sleep(4)
    machine.reset()
elif transmitTwo=='3':
    display.scroll('big win')
    utime.sleep(4)
    machine.reset()
else:
    machine.reset()
