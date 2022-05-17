from microbit import *
import radio
import random
import utime
radio.on()
radioChannel=0
radio.config(group=radioChannel)
a=True
while a:
    transmit=radio.receive()
    if transmit=='1':
        a=False

b=random.randint(0,9)
radio.send(str(b))

radio.config(group=10)
a=True
while a:
    transmitTwo=radio.receive()
    if transmitTwo=='1'or transmitTwo=='2' or transmitTwo=='3':
        a=False
        n=1


zero=Image("50505:"
    "05050:"
    "50505:"
    "05050:"
    "50505")

one=Image("00000:"
    "05050:"
    "05550:"
    "00500:"
    "00000")

two=Image("00500:"
    "05050:"
    "50005:"
    "05050:"
    "00500")

three=Image("00000:"
    "05550:"
    "05050:"
    "05550:"
    "0000")

four=Image("00000:"
    "55555:"
    "00000:"
    "55555:"
    "00000")

five=Image("05005:"
    "50050:"
    "00500:"
    "05005:"
    "50050")

six=Image("05050:"
    "05050:"
    "05050:"
    "05050:"
    "05050")

seven=Image("05050:"
    "05050:"
    "50005:"
    "05550:"
    "00000")

eight=Image("55505:"
    "50005:"
    "50505:"
    "50505:"
    "50505")

nine=Image("50505:"
    "05550:"
    "55555:"
    "05550:"
    "50505")




symbols=[one,two,three,four,five,six,seven,eight,nine]
def cycle(c,symbols):
    for i in range(5):
        display.show(symbols,delay=100)
    display.show(symbols[c])

if n==1:
    cycle(b,symbols)

utime.sleep(4)

if transmitTwo=='2':
    display.scroll('win')
elif transmitTwo=='3':
    display.scroll('big win')
