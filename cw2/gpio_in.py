import select
import gpio4

gpio27 = gpio4.SysfsGPIO(27)
gpio27.export = True # use the pin
gpio27.direction = 'out' # set direction to output
f=open("/sys/class/gpio/gpio27/value","r")
e=select.epoll()
e.register(f,select.EPOLLPRI)
while True:
    print(f.read())
    e.poll()
    f.seek(0,0)
