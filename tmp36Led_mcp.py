from gpiozero import MCP3008, PWMLED
from time import sleep

pot = MCP3008(channel=0)
LED = PWMLED(21)


while True:
    potmeter = pot.value
    temp = pot.value*3.3
    temp =(temp-0.5)*100 #ik kreeg hier een rare waarde, geen idee hoe dit komt.
    print(temp)
    sleep(1)