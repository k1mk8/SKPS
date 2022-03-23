import gpio4
from time import sleep
import glob

leds = glob.glob('/sys/class/leds/*')
led = gpio4.SysfsLED(leds[0])
led.brightness = led.max_brightness