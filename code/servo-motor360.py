import machine, time
from machine import Pin, PWM

servo = machine.PWM(Pin(5), freq=200, duty=550)
time.sleep(5)

servo.deinit()


