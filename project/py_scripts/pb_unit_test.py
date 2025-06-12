from pedestrian_button import Pedestrian_Button
from machine import Pin
from time import sleep, time
'''
led_r = Pin(3, Pin.OUT)
led_y = Pin(5, Pin.OUT)
led_g = Pin(7, Pin.OUT)
led_w = Pin(17, Pin.OUT)
led_s = Pin(19, Pin.OUT)
'''
button = Pedestrian_Button(22, True)

print('testing button')
while True:
    button.button_state
    sleep(0.5)