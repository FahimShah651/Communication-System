import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Given parameters
Omega_N = 4000  # Maximum frequency in Hz
M = 3           # Downsampling factor
L = 2           # Upsampling factor

# Calculate sampling period
Ts = 1 / Omega_N

# Define the original signal X(Ω) as a triangular pulse (same as Exercise 2)
Omega = np.linspace(-Omega_N, Omega_N, 1000)
X_Omega = np.zeros_like(Omega)
X_Omega[np.logical_and(Omega >= -Omega_N, Omega <= 0)] = (Omega[np.logical_and(Omega >= -Omega_N, Omega <= 0)] + Omega_N) / Omega_N
X_Omega[np.logical_and(Omega > 0, Omega <= Omega_N)] = (Omega_N - Omega[np.logical_and(Omega > 0, Omega <= Omega_N)]) / Omega_N

# Perform downsampling (same as Exercise 2)
X_downsampled = X_Omega[::M]
Omega_downsampled = Omega[::M]

# Perform upsampling by inserting zeros
upsampled_length = len(X_downsampled) * L
X_upsampled = np.zeros(upsampled_length)*3
X_upsampled[::L] = X_downsampled

# Upsample the Omega array accordingly
Omega_upsampled = np.linspace(-Omega_N, Omega_N, upsampled_length)*3

# Plot the original and upsampled signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(Omega, X_Omega, label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Omega')
plt.ylabel('X(Omega)')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(Omega_upsampled, X_upsampled, label='Upsampled Signal', drawstyle='steps-post')
plt.title('Upsampled Signal')
plt.xlabel('Omega')
plt.ylabel('X_upsampled(Omega)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
