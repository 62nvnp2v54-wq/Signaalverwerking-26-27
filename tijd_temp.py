import time as time
from time import sleep
import board
import digitalio
from adafruit_bme280 import basic as adafruit_bme280
import csv

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)

bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)

bestand = open("/home/rpi/Documents/bme280_data.csv", "a")
csv_writer = csv.writer(bestand)

while True:
    huidige_tijd = time.ctime()
    print(huidige_tijd)
    print(f"    temp: {bme280.temperature:.1f} C")
    print(f"    humid: {bme280.humidity:.1f} %")
    print(f"    pressure: {bme280.pressure:.1f} hPa")
    print()

    csv_writer.writerow([huidige_tijd, f"{bme280.temperature:.1f}", f"{bme280.humidity:.1f}", f"{bme280.pressure:.1f}"])
    bestand.flush()

    sleep(1)
