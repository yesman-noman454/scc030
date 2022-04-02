from microbit import *
import radio
radio.config(channel=1)
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
def cycle(a):
    for i in range(5):
        display.show(symbols,delay=100)
    display.show(symbols[a])

while True:
    transmit=radio.recive()
    if transmit!="None" and len(transmit)!=0:
        cycle(transmit)
