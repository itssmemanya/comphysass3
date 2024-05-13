import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('noise.txt')

dft = np.fft.fftshift(np.fft.fft(data, norm='ortho'))
freq = np.fft.fftshift(np.fft.fftfreq(len(data)))
power_spectrum = np.abs(dft) ** 2

n = 10
bins = np.linspace(freq.min(), freq.max(), n + 1)
binned_power_spectrum = []

for i in range(n):
    bin_indices = np.where(np.logical_and(freq >= bins[i], freq < bins[i + 1]))
    bin_power_spectrum = power_spectrum[bin_indices]
    bin_mean = np.mean(bin_power_spectrum)
    binned_power_spectrum.append(bin_mean)

mean_freq = (bins[:-1] + bins[1:]) / 2

plt.subplot(3,1,1)
plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Noise')

plt.subplot(3,1,2)
plt.plot(freq, abs(dft), label='DFT')
plt.plot(freq, power_spectrum, label='Power Spectrum')
plt.xlabel('Frequency (k)')
plt.ylabel('Magnitude')
plt.legend()

plt.subplot(3,1,3)
plt.hist(mean_freq, bins=bins, weights=binned_power_spectrum)
plt.xlabel('Frequency(k)')
plt.ylabel('Binned Power')
plt.show()
