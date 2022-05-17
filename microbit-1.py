from microbit import *
import radio
radio.on()
def on_button_pressed_a():
    display.show('0')
    each=[]
    display.show('1')
    for i in range(0,3):
        display.show('2')
        radio.config(group=i)
        display.show('3')
        radio.send('1')
        display.show('4')
        a=True
        display.show('5')
        while a:
            display.show(i)
            transmit=radio.receive()
            if transmit=='0' or  transmit=='1' or  transmit=='2' or  transmit=='3' or  transmit=='4' or  transmit=='5' or  transmit=='6' or  transmit=='7' or  transmit=='8' or  transmit=='9':
                a=False
                display.show('8')
                each.append(transmit)
                transmit=''
    radio.config(group=10)
    if each[0]==each[1]==each[2]:
        display.show('10')
        radio.send('3')
    elif each[0]==each[1]:
        display.show('11')
        radio.send('2')
    elif each[0]==each[1]:
        display.show('12')
        radio.send('2')
    elif each[1]==each[2]:
        display.show('13')
        radio.send('2')
    else:
        display.show('14')
        radio.send('1')



while True:
    if button_a.is_pressed():
        display.show(Image.HEART)
        on_button_pressed_a()
