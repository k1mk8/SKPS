from random import uniform
from time import sleep
filepath = './voltage.txt'

def generate_changing_voltage():
    f = open(filepath, "w")
    for i in range(10):
        x = uniform(2,5)
        f.write(str(x))
        f.write(";")
        sleep(0.2)

if __name__ == "__main__":
    generate_changing_voltage()
