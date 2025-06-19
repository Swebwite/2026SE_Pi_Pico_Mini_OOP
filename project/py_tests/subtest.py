from controller import TrafficLightSystem, PedestrianSubsystem
from led_light import Led_Light
from audio_notification import Audio_Notification
from pedestrian_button import Pedestrian_Button
from machine import Pin
from time import sleep, time


led_tr = Led_light(3, False, True)
led_ta = Led_light(5, False, True)
led_tg = Led_light(7, False, True)
led_pg = Led_light(17, False, True)
led_pr = Led_light(19, False, True)
buzzer = Audio_Notification(27, True)
button = Pedestrian_Button(22, True)

def Subsystem_Driver():
    print('testing idle')
    