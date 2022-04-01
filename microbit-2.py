from microbit import *
import radio
radio.config(channel=0)
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

four=Image()

five=Image()

six=Image()

seven=Image()

eight=Image()

nine=Image()

symbols=[one,two,three,four,five,six,seven,eight,nine]
def cycle(a):
    for i in range(5):
        display.show(symbols,delay=100)
    display.show(symbols[a])

while True:
    transmit=radio.recive()
    if transmit!="None" and len(transmit)!=0:
        cycle(transmit)
