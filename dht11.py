from machine import Pin
from dht import DHT11
import time

sensor = DHT11(Pin(15))

def read_once():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    now = time.localtime()
    timestamp = "{:04}/{:02}/{:02} {:02}:{:02}:{:02}".format(*now[:6])
    return f"{timestamp} 温度: {temp} C 湿度: {hum} %"