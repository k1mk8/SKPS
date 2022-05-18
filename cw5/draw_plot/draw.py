import matplotlib.pyplot as plt
from time import sleep
filepath = './voltage.txt'

def draw_plot():
    punkty = []
    f = open(filepath, "r")
    liczba = ""
    while(f.read()):
        znak = f.read(1)
        if znak != ";":
            liczba = liczba + znak
        else:
            rys = int(liczba)
            liczba = ""
            print(rys)
            punkty.append(rys)
            plt.plot(punkty)
            plt.title("Napiecie")
            plt.show()
            sleep(0.2)