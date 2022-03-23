import periphery
import time
from math import sin, pi

led = periphery.GPIO("/dev/gpiochip0", "GPIO27", "out")

for i in range(50):
    duty_cycle = sin((pi/12)*i)
    led.write(True)
    while time.monotonic_ns() < duty_cycle:
        pass
    periphery.sleep(1)
    led.write(False)
    while time.monotonic_ns() < (0.2 - duty_cycle):
        pass
    periphery.sleep(1)

    