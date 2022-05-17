from microbit import *
import radio
radio.on()
def on_button_pressed_a():
    each=[]
    for i in range(0,2):
        radio.config(group=i)
        radio.send_bytes(1)
        a=True
        while a:
            transmit=radio.recive()
            if transmit!="None" and len(transmit) != 0:
                a=False
                each.append(transmit)
                transmit=''
    radio.config(group=10)
    if each[0]==each[1]==each[2]:
        radio.send_bytes(3)
    elif each[0]==each[1] or each[0]=each[2] or each[1]==each[2]:
        radio.send_bytes(2)
    else:
        radio.send_bytes(1)



while True:
    if microbit.button_a.is_pressed():
        on_button_pressed_a()
