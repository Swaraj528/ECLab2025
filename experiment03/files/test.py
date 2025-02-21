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
        y.append(20*math.log10(float(line[1])))
plt.scatter(x, y)
t = np.linspace(0, 10, 10000)
plt.plot(t, -10*np.log10(1 + (RC**2)*np.power(10, 2*t)))
plt.xlim(0, 5)
plt.ylim(-25, 1)
t=np.linspace(0, -math.log10(RC))
plt.plot(t, 0*t)
t=np.linspace(-math.log10(RC), 5)
plt.plot(t, -20*math.log10(RC) -20*t)
#plt.xlim(0, 10)
plt.savefig("fit.png")
plt.show()
