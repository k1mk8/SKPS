import matplotlib.pyplot as plt
from time import sleep
from generate_voltage import generate_changing_voltage 
filepath = './voltage.txt'

PERIOD = 0.2

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
            sleep(PERIOD)
    input()

def main():
    generate_changing_voltage()
    draw_plot()

if __name__ == "__main__":
    main()
