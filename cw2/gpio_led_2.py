from periphery import PWM
fromt math import sin, pi
from time import sleep

pwm = PWM(0, 10)

for i in range(50):
    pwm.duty_cycle = abs(sin(pi/12)*i)
    sleep(0.2)