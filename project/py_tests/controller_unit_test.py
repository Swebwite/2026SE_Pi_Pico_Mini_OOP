from controller import Controller
from led_light import Led_Light
from audio_notification import Audio_Notification
from pedestrian_button import Pedestrian_Button
from machine import Pin
from time import sleep, time


led_tr = Led_Light(3, False, False)
led_ta = Led_Light(5, False, False)
led_tg = Led_Light(7, False, False)
led_pg = Led_Light(17, False, False)
led_pr = Led_Light(19, True, False)
buzzer = Audio_Notification(27, False)
button = Pedestrian_Button(22, False)

controller = Controller(led_pr, led_pg, led_tr, led_ta, led_tg, button, buzzer, True)

'''
print('Testing idle state')
controller.set_idle_state()
print('Pass if: pedestrian=RED, traffic=GREEN, buzzer=OFF')
sleep(3)

print('Testing change state')
controller.set_change_state()
print('Pass if: pedestrian=RED, traffic=AMBER, buzzer=OFF')
sleep(3)

print('Testing walk state')
controller.set_walk_state()
print('Pass if: pedestrian=GREEN, traffic=RED, buzzer=ON')
sleep(3)

print('Testing warning state')
controller.set_warning_state()
print('Pass if: pedestrian=WARNING, traffic=RED, buzzer=OFF')
sleep(3)

print('Testing error state')
controller.error_state()
print('Pass if: traffic=AMBER FLASH')
sleep(3)
'''
while True:
    controller.update()