import numpy as np
import matplotlib.pyplot as plt

# Given parameters
Omega_N = 4000  # Maximum frequency in Hz
M = 3           # Downsampling factor

# Calculate sampling period
Ts = 1 / Omega_N

# Define the original signal X(Ω) as a triangular pulse
Omega = np.linspace(-Omega_N, Omega_N, 1000)
X_Omega = np.zeros_like(Omega)
X_Omega[np.logical_and(Omega >= -Omega_N, Omega <= 0)] = (Omega[np.logical_and(Omega >= -Omega_N, Omega <= 0)] + Omega_N) / Omega_N
X_Omega[np.logical_and(Omega > 0, Omega <= Omega_N)] = (Omega_N - Omega[np.logical_and(Omega > 0, Omega <= Omega_N)]) / Omega_N

# Perform downsampling
X_downsampled = X_Omega[::M]
Omega_downsampled = Omega[::M]/3

# Plot the original and downsampled signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(Omega, X_Omega, label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Omega')
plt.ylabel('X(Omega)')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.stem(Omega_downsampled, X_downsampled, label='Downsampled Signal')
plt.title('Downsampled Signal')
plt.xlabel('Omega')
plt.ylabel('X_downsampled(Omega)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
