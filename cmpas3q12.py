import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.exp(-x**2)

def h(x):
    return np.exp(-4*x**2)

def analytical_convolution(x):
    return np.sqrt(np.pi) / np.sqrt(5) * np.exp(-4*x**2/5)

def dft_convolution(g, h):
    G = np.fft.fft(g)
    H = np.fft.fft(h)
    convolution = np.fft.ifft(G * H).real
    return convolution

N=1000
x = np.linspace(-3, 3, N)

# Zero padding
g = np.pad(g(x), (0, N), mode='constant', constant_values=(0, 0))
h = np.pad(h(x), (0, N), mode='constant', constant_values=(0, 0))

analytical = analytical_convolution(x)
dft = dft_convolution(g, h) * (x[1] - x[0])

plt.plot(x, analytical, label='Analytical Convolution')
plt.plot(x, dft[N//2:3*N//2], label='Convolution via DFT')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
