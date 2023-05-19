#problem 5

ACQTIME = 60.0  # seconds of data acquisition

#    samples per second
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
SPS = 4

nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS

import time
import numpy as np
import matplotlib.pyplot as plt
import board
import adafruit_mcp9808
###############################################################################

print()
print('Initializing ADC...')
print()




indata = np.zeros(nsamples,'float')

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter()
   with board.I2C() as i2c:
       indata[i] = adafruit_mcp9808.MCP9808(i2c).temperature
   while (time.perf_counter() - st) <= sinterval:
      pass

t = time.perf_counter() - t0

xpoints = np.arange(0, ACQTIME, sinterval)

print('Time elapsed: %.9f s.' % t)

filestr = ''
for i in indata:
    filestr += str(i) + '\n'
    
datafile = open('p6_hw7_data.txt','w')
datafile.write(filestr)
datafile.close()

f1, ax1 = plt.subplots()

#
# Default plotting style connects points with lines
#
ax1.plot(xpoints, indata)
ax1.set_title("Temperature over time")
ax1.set_ylabel("Temperature (C)")
ax1.set_xlabel("Time (seconds)")
#
# Plotting with steps is better for visualizing sampling
#
# ax1.plot(xpoints, indata,'-',drawstyle='steps-post')

f1.show()

input("\nPress <Enter> to exit...\n")
