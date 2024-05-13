import numpy as np
import matplotlib.pyplot as plt

# Define the constant function
def constant_function(c,n):
    x=np.ones(n)
    return c * x

c = 2
n=1000

# Compute the Fourier transform of constant function
constant_fft = np.fft.fft(constant_function(c,n))
constant_fft = np.fft.fftshift(constant_fft)
freq = np.fft.fftfreq(n, 0.02)
freq = np.fft.fftshift(freq)
# Plot the results
plt.plot(freq, np.abs(constant_fft))
plt.xlabel('Frequency')
plt.ylabel('Fourier Transform Magnitude')
plt.title('Fourier Transform of Constant Function')
plt.show()
