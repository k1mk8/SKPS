import matplotlib.pyplot as plt
from pwm import pwm_frequency, pwm_duty_cycle


FREQUENCY_LIST = [2, 4, 6, 8, 6, 4, 2]
FREQUENCY = 2

DUTY_CYCLES = [0.5, 0.3, 0.1, 0.1, 0.3, 0.5]
DUTY_CYCLE = 0.5


def plotter(result: list):
    times = [value[0] for value in result]
    time = [0.0, 0.0]
    values = [value[1] for value in result]
    value = [0.0, 1.0]
    for i in range(len(times)):
        time.append(time[-1] + times[i])
        time.append(time[-1])
        value.append(values[i])
        if values[i] == 1.0:
            value.append(0.0)
        else:
            value.append(1.0)
    plt.yticks([0, 1])
    plt.xlabel("time")
    plt.ylabel("value")
    plt.plot(time, value)
    plt.savefig('pwm.pdf')
    plt.show()


def plot_pwm_duty_cycle(duty_cycles, freq):
    result = pwm_duty_cycle(duty_cycles, freq)
    plotter(result)


def plot_pwm_frequency(frequency_list, duty_cycle):
    result = pwm_frequency(frequency_list, duty_cycle)
    plotter(result)


def main():
    plot_pwm_frequency(FREQUENCY_LIST, DUTY_CYCLE)
    # plot_pwm_duty_cycle(DUTY_CYCLES, FREQUENCY)


if __name__ == '__main__':
    main()
