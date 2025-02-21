import matplotlib.pyplot as plt 
import numpy as np 
import math 
import csv 

x = list()
y = list()
i = 0
RC = 1e4*58.5*1e-9
with open("data.csv", "r") as file:
    for line in csv.reader(file):
        if (i == 0):
            i = 1
            continue
        x.append(math.log10(2*math.pi*float(line[0])))
        y.append(-2 * np.pi * float(line[0]) * float(line[2]) * 1e-6)
plt.scatter(x, y)
t = np.linspace(0, 10, 10000)
plt.plot(t, -np.atan(np.power(10, t) * RC))
plt.savefig("phase_1.png")
plt.show()
