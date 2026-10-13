from gpiozero import LED, Button
from signal import pause
teller = 0
led1 = LED(4)
button = Button(5)

def teller_1():
    global teller
    teller += 1
    millis = teller % 2
    if millis == 1:
        led1.on()
    else:
        led1.off()
    print(millis)

button.when_pressed = teller_1
pause()