from machine import Pin, PWM
from time import sleep, time

class Audio_Notification(PWM):
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0) # Start with buzzer off
        self.__last_toggle_time = time()
    
    def warning_on(self):
        if self.__debug:
            print('Warning on') # debug message
        now = time()
        if now - self.__last_toggle_time >= 0.5: #checks if it has been 0.5s or more
            self.beep(freq=500, duration=500)
            self.__last_toggle_time = now # resets last toggle time
    
    def warning_off(self):
        if self.__debug:
            print('Warning off') # debug message
        self.duty_u16(0) # turn off sound

    def beep(self, freq=1000, duration=500):
        # beeps for 500 ms
        if self.__debug:
            print('Beep') # debug message
        self.freq(freq)
        self.duty_u16(32768) # 50% duty cycle
        sleep(duration / 1000)
        self.duty_u16(0) # turn off buzzer