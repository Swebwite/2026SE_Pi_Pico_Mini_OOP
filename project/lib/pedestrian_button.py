from machine import Pin
from time import ticks_ms, ticks_diff

class Pedestrian_Button(Pin):
    # child class inherits the parent 'Pin' class
    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0
        self.__pedestrian_waiting = False
        self.button_state
        # Set up interrupt on rising edge
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    @property
    # gets the buttons state
    def button_state(self):
        if self.__debug:
            print(f'Button connected to pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}')
        return self.__pedestrian_waiting
    
    @button_state.setter
    # sets the buttons state
    def button_state(self, value):
        self.__pedestrian_waiting = value
        if self.__debug:
            print(f'Button state on pin {self.__pin} set to {value}')
    
    def callback(self, pin):
        # catches a button press and passes that a pedestrian is waiting
        current_time = ticks_ms()
        if (ticks_diff(current_time, self.__last_pressed) > 200):
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f'Button pressed on pin {self.__pin} at {current_time}ms')
