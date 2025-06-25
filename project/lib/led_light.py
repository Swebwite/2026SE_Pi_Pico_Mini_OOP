from machine import Pin
from time import sleep, time

class Led_Light(Pin):
    # Sub Class inherits the 'Pin' Class
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.__last_toggle_time = 0

    def on(self):
        # method overriding polymorphism of the Super Class
        self.high()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is high")

    def off(self):
        # method overriding polymorphism of the Super Class
        self.low()
        if self.__debug:
            print(f"LED connected to Pin {self.__pin} is low")

    def toggle(self):
        # method overriding polymorphism of the Super Class
        if self.value() == 0:
            self.on()
        elif self.value() == 1:
            self.off()

    @property
    def led_light_state(self):
        # Getter method
        return self.value()

    @led_light_state.setter
    def led_light_state(self, value):
        # Setter method
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

    def flash(self):
        now = time()
        if self.__flashing and now - self.__last_toggle_time >= 0.5:
            self.toggle()
            self.__last_toggle_time = now