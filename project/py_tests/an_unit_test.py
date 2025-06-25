from time import sleep
from audio_notification import Audio_Notification

buzzer = Audio_Notification(27, True)

print('testing beep')
buzzer.beep()
sleep(1)

print('testing warning on')
buzzer.warning_on()
sleep(1)

print('testing warning off')
buzzer.warning_off()
sleep(1)