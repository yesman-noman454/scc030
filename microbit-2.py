from microbit import *
import radio
radio.on()
radioChannel=0
radio.config(channel=radioChannel)
a=True
while a:
    transmit=radio.recive()
    if transmit!="None" and len(transmit)!=0:
        a=False

##Needs to do the selection process for what output
b=randint(0,9)
radio.send_number(b)
#a=True
#while a:
#    transmitOne=radio.recive()
#    if transmitOne!="None" and len(transmitOne)!=0:
#        a=False
#        if transmitOne == 1:
#            b=randint(0,9)
#            radio.send_number(b)

radio.config(channel=10)
a=True
while a:
    transmitTwo=radio.recive()
    if transmitTwo!="None" and len(transmitTwo)!=0:
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


wLetter=Image("50005:"
    "50005:"
    "50005:"
    "50505:"
    "55055")

iLetter=Image("55555:"
    "00500:"
    "00500:"
    "00500:"
    "55555")

nLetter=Image("50005:"
    "55005:"
    "50505:"
    "50055:"
    "50005")

bLetter=Image("55550:"
    "50005:"
    "55555:"
    "50005:"
    "55550")
gLetter=Image("55555:"
    "50000:"
    "50555:"
    "50005:"
    "55555")

symbols=[one,two,three,four,five,six,seven,eight,nine]

win=[wLetter,iLetter,gLetter]

big=[bLetter,iLetter,gLetter]

bigwin[big[radioChannel],win[radioChannel]]

def cycle(c,symbols):
    for i in range(5):
        display.show(symbols,delay=100)
    display.show(symbols[c])

if n==1:
    cycle(b,symbols)

control.wait_micros(4000)

if transmitTwo==2:
    display.show(win[radioChannel])
elif transmitTwo==3:
    display.show(bigwin,delay=100)
