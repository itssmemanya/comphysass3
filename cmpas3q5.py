import numpy as np
import time
import matplotlib.pyplot as plt
import cmath

j=complex(0,1)

# Direct computation of DFT
def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-j * np.pi * k * n / N)/np.sqrt(N)
    return np.dot(e, x)

# Function to compute DFT using numpy.fft.fft
def fft(x):
    return np.fft.fft(x, norm='ortho')

# Measure time taken by direct DFT computation
def time_dft(x):
    start_time = time.time()
    dft(x)
    return time.time() - start_time

# Measure time taken by numpy.fft.fft
def time_fft(x):
    start_time = time.time()
    fft(x)
    return time.time() - start_time

n_values = np.arange(4, 129)
time_direct = []
time_numpy = []

# Iterate over n values
for n in n_values:
    # Generating random numbers for dft and fft
    x = np.random.rand(n)
    time_direct.append(time_dft(x))
    time_numpy.append(time_fft(x))

# Plotting results
plt.plot(n_values, time_direct, label='Direct DFT Computation')
plt.plot(n_values, time_numpy, label='NumPy FFT')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time Taken by DFT Methods vs n')
plt.legend()
plt.show()
