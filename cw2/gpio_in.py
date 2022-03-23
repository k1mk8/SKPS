import select
import gpio4
from time import sleep

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' # set direction to output
f=open("/sys/class/gpio/gpio27/value","r")
e=select.epoll()
e.register(f,select.EPOLLPRI)
while True:
    print(f.read())
    e.poll()
    gpio27.value = 1
    sleep(0.5)
    gpio27.value = 0
    f.seek(0,0)
