from w1thermsensor import W1ThermSensor, Unit
from gpiozero import LEDBoard
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)
LedRed = LEDBoard(17)
LedOrange = LEDBoard(27)
LedGreen = LEDBoard(22)

sensor = W1ThermSensor()
while True:
    try:
        temperature_c = dhtDevice.temperature
    except RuntimeError as error:
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    temperature_in_celsius = sensor.get_temperature()
    time.sleep(2.0)
    print(f"DS18B20: {temperature_in_celsius}, DHT11: {temperature_c}")
    verschil = abs(temperature_in_celsius - float(temperature_c))
    if (verschil <1):
        LedGreen.on()
        LedRed.off()
        LedOrange.off()
    elif (verschil >= 1 and verschil < 5):
        LedOrange.on()
        LedRed.off()
        LedGreen.off()
    else:
        LedRed.on()
        LedOrange.off()
        LedGreen.off()