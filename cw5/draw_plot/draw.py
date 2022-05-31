import matplotlib.pyplot as plt
from time import sleep
filepath = './voltage.txt'

def draw_plot():
    punkty = []
    f = open(filepath, "r")
    liczba = ""
    data = f.read()
    plt.ion()
    fig, ax = plt.subplots()
    plt.title("Napiecie")
    for znak in data:
        if znak != ";":
            liczba += znak
        else:
            rys = float(liczba)
            liczba = ""
            punkty.append(rys)
            ax.plot(punkty)
            fig.canvas.draw()
            fig.canvas.flush_events()
            sleep(0.2)

if "__name__" == "__main__":
    draw_plot()