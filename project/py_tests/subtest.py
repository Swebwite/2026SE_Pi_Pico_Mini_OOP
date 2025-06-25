from controller import TrafficLightSystem, PedestrianSubsystem
from led_light import Led_Light
from audio_notification import Audio_Notification
from pedestrian_button import Pedestrian_Button
from machine import Pin
from time import sleep, time


led_tr = Led_Light(3, False, True)
led_ta = Led_Light(5, False, True)
led_tg = Led_Light(7, False, True)
led_pg = Led_Light(17, False, True)
led_pr = Led_Light(19, False, True)
buzzer = Audio_Notification(27, True)
button = Pedestrian_Button(22, True)

t_light = TrafficLightSystem(led_tr, led_ta, led_tg, False)
p_light = PedestrianSubsystem(led_pr, led_pg, button, buzzer, False)

def Traffic_Subsystem_Driver():
    print('testing traffic light')
    sleep(2)
    t_light.show_red()
    print('Pass if: red ON, amber OFF, green OFF')
    sleep(5)
    t_light.show_amber()
    print('Pass if: red OFF, amber ON, green OFF')
    sleep(5)
    t_light.show_green()
    print('Pass if: red OFF, amber OFF, green ON')
    sleep(5)

def Pedestrian_Subsystem_Driver():
    print('testing pedestrian light')
    sleep(2)
    p_light.show_stop()
    print('Pass if: red ON, green OFF, buzzer OFF')
    sleep(4)
    p_light.show_walk()
    print('Pass if: red OFF, green ON, buzzer ON')
    sleep(4)
    p_light.show_warning()
    print('Pass if: red FLASH, green OFF, buzzer OFF')
    sleep(4)

Traffic_Subsystem_Driver()
Pedestrian_Subsystem_Driver()