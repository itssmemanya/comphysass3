import numpy as np
import matplotlib.pyplot as plt

# Defining the sinc function
def sinc(x):
    return np.where(x == 0, 1, np.sin(x) / x)

# Defining Box function (Analytical Fourier Transform of sinc)
def box(x,a):
    return np.where(abs(x)<a,np.pi/2,0)

x = np.linspace(-30, 30, 1000)

sinc_fft = np.fft.fft(sinc(x), norm='ortho')
sinc_fft = np.fft.fftshift(sinc_fft)
freq = np.fft.fftfreq(len(x), x[1] - x[0])
freq = np.fft.fftshift(freq)

analytical=box(freq,1/(2*np.pi))

plt.plot(freq, abs(np.real(sinc_fft)), label='Numerical')
plt.plot(freq, analytical, label='Analytical', linestyle='--')
plt.xlabel('Frequency')
plt.ylabel('Fourier Transform')
plt.legend()
plt.show()
