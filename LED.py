from machine import Pin
import time

led = Pin('LED', Pin.OUT)
def led_on():
        led.on()
 
def led_off():
        led.off()

def led_blink():
    while True:
        led_on()
        time.sleep(1)
        led_off()
        time.sleep(1)
        

