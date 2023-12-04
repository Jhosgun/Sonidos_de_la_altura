import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 0.01  # Mass of the ball (kg)
g = 9.81  # Acceleration due to gravity (m/s^2)
h = 120  # Initial height (m)
alpha = 0.98  # Coefficient of restitution
k = 95  # Constant for decibel calculation
num_impacts = 10  # Number of impacts to simulate

# Initial conditions
E0 = m * g * h  # Initial potential energy
times = [0]  # Times of impacts
energies = [E0]  # Energies at each impact
heights = [h]  # Heights at each impact
decibels = [(   30*np.log10(2) + 10*np.log10(120) + 95   )*(np.pi/4)]  # Sound power in decibels

# Simulation
for n in range(1, num_impacts):
    En = alpha**(n - 1) * E0  # Energy at nth impact
    energies.append(En)
    decibels.append(10 * np.log10(En))
    
    # Time for each impact
    t_n = times[n - 1] + np.sqrt(2 * alpha**(n - 1) * h / g)
    times.append(t_n)
    heights.append(0)  # Impact at ground level

# Plotting
plt.figure(figsize=(12, 6))

# Energy plot
plt.subplot(1, 2, 1)
plt.plot(times, energies, 'o-', label='Energy')
plt.xlabel('Tiempo (s)')
plt.ylabel('Energía (J)')
plt.title('Energía en cada impacto')
plt.grid(True)

# Decibels plot
plt.subplot(1, 2, 2)
plt.plot(times, decibels, 'o-', color='orange', label='Decibels')
plt.xlabel('Tiempo (s)')
plt.ylabel('Decibeles (DB)')
plt.title('Decibeles en cada impacto')
plt.grid(True)

plt.tight_layout()
plt.show()

