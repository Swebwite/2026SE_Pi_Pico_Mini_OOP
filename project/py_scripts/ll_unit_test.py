from led_light import Led_Light
from machine import Pin
from time import sleep, time

led_r = Pin(3, Pin.OUT)
led_y = Pin(5, Pin.OUT)
led_g = Pin(7, Pin.OUT)

print('testing on')
led_r.on()
sleep(0.3)
led_y.on()
sleep(0.3)
led_g.on()
sleep(1)

print('testing off')
led_r.off()
sleep(0.3)
led_y.off()
sleep(0.3)
led_g.off()
sleep(1)