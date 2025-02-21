import matplotlib.pyplot as plt 
import numpy as np 
import math 
import csv 

x = list()
y = list()
i = 0
RC = 1e4*220*1e-9
with open("data_3.csv", "r") as file:
    for line in csv.reader(file):
        if (i == 0):
            i = 1
            continue
        x.append(math.log10(2*math.pi*float(line[0])))
        y.append(20*math.log10(float(line[1])))
plt.scatter(x, y)
t = np.linspace(0, 4, 10000)
#plt.plot(t, -10*np.log10((1 + (RC ** 2 * np.power(10, 2*t))) * (((4 * (np.power(10, t) * RC)**2 + 1)**2) + ((5 * np.power(10, t) * RC) + 2 * ((2 * np.power(10, t) * RC)**3) + 2 * (2 * np.power(10, t) * RC)**2)**2)))
#plt.plot(t, -30*np.log10(1 + (RC**2)*np.power(10, 2*t)))
plt.plot(t, -10*np.log10((1 - 5 * (np.power(10, t) * RC) ** 2)**2 + (6 * RC * np.power(10, t) - (np.power(10, t) * RC) ** 3)))
plt.savefig("fit_3.png")
plt.show()
