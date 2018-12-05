import time

from pid import PIDArduino
from kettle import Kettle
from recipe import Recipe

def main():
    setpoint = 65
    tempinicial = 60

    count = 0

    panela = Kettle(30,16, tempinicial)

    pid = PIDArduino(1, 51.17, 0.16, 243.43, 0.0, 1023.0)
    output = pid.calc(tempinicial, setpoint)
    print(output)
    delay = 1
    time.sleep(delay)
    while (True):
        panela.heat(5 * (output / 100), delay)
        panela.cool(delay, 30)
        output = pid.calc(panela.temperature, setpoint)
        print('output: ' + str(output))
        print('temperatura panela: ' + str(panela.temperature))
        print('contador: ' + str(count))
        count += 1
        if count == 700:
            setpoint = 79
        if count == 1000:
            setpoint = 100
        time.sleep(delay)

if __name__ == '__main__':
    main()