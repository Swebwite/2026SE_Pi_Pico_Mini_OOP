from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

class TrafficLightSystem:
    def __init__(self, red, amber, green, debug=False):
        self.__red = red
        self.__amber = amber
        self.__green = green
        self.__debug = debug
        
    def show_red(self):
        if self.__debug:
            print('Traffic: Red ON')
        self.__red.on()
        self.__amber.off()
        self.__green.off()

    def show_amber(self):
        if self.__debug:
            print('Traffic: Amber ON')
        self.__red.off()
        self.__amber.on()
        self.__green.off()

    def show_green(self):
        if self.__debug:
            print('Traffic: Green ON')
        self.__red.off()
        self.__amber.off()
        self.__green.on()


class PedestrianSubsystem:
    def __init__(self, red, green, button, buzzer, debug=False):
        self.__red = red
        self.__green = green
        self.__button = button
        self.__buzzer = buzzer
        self.__debug = debug
    
    def show_stop(self):
        if self.__debug:
            print("Pedestrian: Red ON")
        self.__red.on()
        self.__green.off()
        self.__buzzer.warning_off()

    def show_walk(self):
        if self.__debug:
            print("Pedestrian: Green ON, Warning ON")
        self.__red.off()
        self.__green.on()
        self.__buzzer.warning_on()

    def show_warning(self):
        if self.__debug:
            print("Pedestrian: Red FLASHING")
        self.__red.flash()
        self.__green.off()
        self.__buzzer.warning_off()

    def is_button_pressed(self):
        return self.__button.button_state()

    def reset_button(self):
        self.__button.button_state(False)

class Controller:
    def __init__(self, pred, pgreen, tred, tamber, tgreen, button, buzzer, debug=False):
        self.__traffic_lights = TrafficLightSystem(tred, tamber, tgreen, debug=False)
        self.__pedestrian_signals = PedestrianSubsystem(pred, pgreen, button, buzzer, debug=False)
        self.__debug = debug
        self.state = 'IDLE'
        self.last_state_change = time()

    def set_idle_state(self):
        if self.__debug:
            print('System: IDLE State')
        self.__traffic_lights.show_green()
        self.__pedestrian_signals.show_stop()
    
    def set_change_state(self):
        if self.__debug:
            print('System: CHANGE State')
        self.__traffic_lights.show_amber()    
        self.__pedestrian_signals.show_stop()
    
    def set_walk_state(self):
        if self.__debug:
            print('System: WALK State')
        self.__traffic_lights.show_red()    
        self.__pedestrian_signals.show_walk()

    def set_warning_state(self):
        if self.__debug:
            print('System: WARNING State')
        self.__traffic_lights.show_red()    
        self.__pedestrian_signals.show_warning()

    def error_state(self):
        print('System: ERROR State')
        self.__traffic_lights.show_amber() # make flash