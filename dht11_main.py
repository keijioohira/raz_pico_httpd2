from machine import Pin
from dht import DHT11
from aqm0802a import AQM0802A
from machine import I2C, Pin
import time

sensor = DHT11(Pin(15))

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temp:", temp, "C")
    print("Humidity:", hum, "%")

    # LCD初期化
    i2c = I2C(0, scl=Pin(1), sda=Pin(0))
    lcd = AQM0802A(i2c)
    lcd.clear()
    lcd.write(f"T: {temp}C")
    lcd.set_cursor(0, 1)
    lcd.write(f"H: {hum}%")
    
    time.sleep(2)
