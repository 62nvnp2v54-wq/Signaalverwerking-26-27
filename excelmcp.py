from gpiozero import MCP3008, PWMLED
from time import sleep

pot = MCP3008(channel=0)
LED = PWMLED(21)


while True:
    potmeter = pot.value
    print(potmeter)

    LED.value = 1
    sleep(potmeter)
    LED.value = 0
    sleep(potmeter)
