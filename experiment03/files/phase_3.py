import matplotlib.pyplot as plt 
import numpy as np 
import math 
import csv 

x = list()
y = list()
i = 0
RC = 1e4*216*1e-9
with open("data_3.csv", "r") as file:
    for line in csv.reader(file):
        if (i == 0):
            i = 1
            continue
        x.append(math.log10(2*math.pi*float(line[0])))
        y.append(-np.atan(np.tan(2 * np.pi * float(line[0]) * float(line[2]) * 1e-6)))
plt.scatter(x, y)
t = np.linspace(0, 10, 10000)
#plt.plot(t, -np.atan((3 * np.power(10, t) * RC)/(1 - 3 * RC ** 2 * np.power(10, 2*t) - np.power(10, 3*t) * RC **3)))
plt.plot(t, -np.atan((6 * np.power(10, t) * RC - (np.power(10, t) * RC)**3)/(1 - 5 * (np.power(10, t) * RC) ** 2)))
plt.savefig("phase_3.png")
plt.show()
