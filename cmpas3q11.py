import numpy as np
import matplotlib.pyplot as plt

def box(x):
    return np.where(np.logical_and(x > -1, x < 1), 1, 0)

def convolution(f, g):
    return np.convolve(f, g, 'same')

x = np.linspace(-3, 3, 1000)
f = box(x)
conv_result = convolution(f, f) / len(x)  

# Plot the box function and its convolution
plt.plot(x, f, label='Box Function')
plt.plot(x, conv_result, label='Convolution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Convolution of Box Function with Itself')
plt.legend()
plt.show()
