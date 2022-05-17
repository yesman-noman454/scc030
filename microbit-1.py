from microbit import *
import radio
radio.on()
def on_button_pressed_a():
    each=[]
    for i in range(0,2):
        radio.config(group=i)
        radio.send('1')
        a=True
        while a:
            transmit=radio.receive()
            if transmit=='0' or  transmit=='1' or  transmit=='2' or  transmit=='3' or  transmit=='4' or  transmit=='5' or  transmit=='6' or  transmit=='7' or  transmit=='8' or  transmit=='9':
                a=False
                each.append(transmit)
                transmit=''
    radio.config(group=10)
    if each[0]==each[1]==each[2]:
        radio.send('3')
    elif each[0]==each[1]:
        radio.send('2')
    elif each[0]==each[1]:
        radio.send('2')
    elif each[1]==each[2]:
        radio.send('2')
    else:
        radio.send('1')



while True:
    if button_a.is_pressed():
        on_button_pressed_a()
        display.show(Image.HEART)
