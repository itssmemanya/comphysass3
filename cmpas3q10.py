import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
j=complex(0,1)

# Define Gaussian function
def gaussian(x, y):
    return np.exp(-(x**2 + y**2))
# Define Gaussian FT
def gaussian_ft(kx, ky):
    return np.exp(-(np.pi)**2*(kx**2 + ky**2))

x = np.linspace(-10, 10, 128)
y = np.linspace(-10, 10, 128)
X, Y = np.meshgrid(x, y)
f_xy = gaussian(X, Y)


fourier_transform = np.fft.fft2(f_xy, norm='ortho')
fourier_transform = np.fft.fftshift(fourier_transform)
freq = np.fft.fftfreq(len(x), x[1] - x[0])
freq = np.fft.fftshift(freq)

factor = np.abs(np.real(np.exp(-j*freq*np.pi*-10)))
KX, KY = np.meshgrid(freq, freq)
F_kxky= gaussian_ft(KX, KY)

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot_surface(KX, KY, factor*np.abs(fourier_transform), cmap='viridis')
ax.set_xlabel('kx')
ax.set_ylabel('ky')
ax.set_zlabel('Fourier Transform Numrical')
ax = fig.add_subplot(1,2,2, projection='3d')
ax.plot_surface(KX, KY, F_kxky, cmap='plasma')
ax.set_xlabel('kx')
ax.set_ylabel('ky')
ax.set_zlabel('Fourier Transform Analytical')
plt.show()
