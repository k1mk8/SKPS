from cmath import sin
import gpio4
from time import sleep
from math import sin, pi

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' # set direction to output
duty_cycle = 0.0
for i in range(10):
    gpio27.value = 1 # set value to high
    x = 1 * duty_cycle
    sleep(1*duty_cycle)
    gpio27.value = 0 # set value to low
    sleep(1-x)
    duty_cycle = sin((pi/6)*i)
gpio27.export = False # cleanup
