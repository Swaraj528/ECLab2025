import matplotlib.pyplot as plt 
import numpy as np 
import csv
import math

# Read CSV Data
x = []
y = []
i = 0
with open("data.csv", "r") as file:
    for line in csv.reader(file):
        if i == 0:  # Skip header
            i = 1
            continue
        x.append(math.log10(float(line[2])))  # log scale of freq
        y.append(20 * np.log10(float(line[1]) / float(line[0])))  # Gain in dB

# Define Theoretical High-Pass Filter Response
def highpass_bode(x):
    R = 22e3  # 22kΩ
    C = 220e-9  # 220nF
    f0 = 1 / (2 * np.pi * R * C)  # Cutoff Frequency
    Q = 0.5  # Q-factor for unity-gain Sallen-Key HPF
    ω0 = 2 * np.pi * f0  # Natural Angular Frequency
    f = np.power(10, x)  # Convert log scale back to linear frequency scale
    ω = 2 * np.pi * f  # Convert to angular frequency

    # High-pass Transfer Function (Magnitude in dB)
    H_mag = (ω**2) / np.sqrt((ω0**2 - ω**2)**2 + (ω0 * ω / Q)**2)
    return 20 * np.log10(H_mag)

# Generate Theoretical Frequency Response
t = np.logspace(0, 3, 1000)  # Frequency from 10 Hz to 100 kHz
theoretical_response = highpass_bode(np.log10(t))

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Measured Data", marker="o", linestyle="None")
plt.plot(np.log10(t), theoretical_response, label="Theoretical Bode Plot", linestyle="-")
plt.xlabel("log10(Frequency (Hz))")
plt.ylabel("Gain (dB)")
plt.title("Sallen-Key High-Pass Filter Bode Plot")
plt.legend()
plt.grid(True)
plt.savefig("high.png")
plt.show()

