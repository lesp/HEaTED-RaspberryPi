import matplotlib.pyplot as plt
from w1thermsensor import W1ThermSensor
from time import sleep
sensor = W1ThermSensor()

x = [0, 1, 2, 3]
y = []

for i in range(4):
    y.append(sensor.get_temperature())
    sleep(1)
    print(y[i])
print(y)    
plt.plot(x,y, 'r', linewidth=6.0)
plt.axis([0,6,0,30])
plt.ylabel('Temperature in C')
plt.xlabel('Seconds')
plt.show()
