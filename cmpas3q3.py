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


with open('Problem_2.txt', 'r') as file:
    data2 = file.readlines()
with open('Problem_3.txt', 'r') as file:
    data3 = file.readlines()

x2_c = []
y2_c = []
x3_c = []
y3_c = []
for line in data2:
    if line.strip():  
        x, y = map(float, line.split(':'))
        x2_c.append(x)
        y2_c.append(y/(4*np.pi))
for line in data3:
    if line.strip():  
        x, y = map(float, line.split(':'))
        x3_c.append(x)
        y3_c.append(y/(4*np.pi))        
        

# Plot all Fourier transform results
plt.plot(freq, abs(np.real(sinc_fft)), label='Numerical Result from NumPy in Problem 1')
plt.plot(freq, analytical, label='Analytical Result from Problem 1', linestyle='--')
plt.plot(x2_c,y2_c, label='Result from C in Problem 2')
plt.plot(x3_c,y3_c, label='Result from C in Problem 3')
plt.xlabel('Frequency')
plt.ylabel('Fourier Transform')
plt.legend()
plt.xlim(-10, 10)  
plt.show()
