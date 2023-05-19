FTIME = 1      # function range in seconds
FS = 920        # samples per second
npts = FTIME*FS  # number of sample points

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import psd

file = open('p5_hw7_data.txt')
data = np.loadtxt(file)
file.close()
mean = np.mean(data)
t = np.linspace(0, FTIME, npts)
y = data-mean
#f1, ax1 = plt.subplots()
#ax1.plot(t,y)
#f1.show()

ny, nx = psd(y, NFFT=npts, Fs=FS, pad_to=16*npts)
f2, ax2 = plt.subplots()
ax2.plot(nx,ny)
ax2.set_title("Power Spectrum Diagram")
ax2.set_ylabel("Power Spectral Density (dB)")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_xlim(0,400)
f2.show()

input("\nPress <Enter> to exit...\n")

#The figure shows that the fundemtal frequency of the light in my room sits at 120 Hz.
