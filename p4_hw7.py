#problem 4

ACQTIME = 1.0  # seconds of data acquisition

#    samples per second
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
SPS = 920

#    full-scale range in mV
#    options: 16:256, 8:512, 4:1024, 2:2048, 1:4096, 2/3:6144.
VGAIN = 1

nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
###############################################################################

print()
print('Initializing ADC...')
print()

i2c = busio.I2C(board.SCL, board.SDA)

#
# Default ADC IC is ADS1015
# Default address is 0x48 on the default I2C bus
#
ads = ADS.ADS1015(i2c)

# Second and third arguments are the ADC channel pins
channel = AnalogIn(ads, ADS.P2, ADS.P3)

# Gain sets the full-scale range in mV (default +/- 6144).
#    options: 16:256, 8:512, 4:1024, 2:2048, 1:4096, 2/3:6144.
#    Note: input should not exceed VDD + 0.3
ads.gain = VGAIN

# Samples per second
#    options: 128, 250, 490, 920, 1600, 2400, 3300.
#
ads.data_rate = SPS

ads.mode = ADS.Mode.CONTINUOUS

indata = np.zeros(nsamples,'float')
vin = AnalogIn(ads, 2, 3)

input('Press <Enter> to start %.1f s data acquisition...' % ACQTIME)
print()

t0 = time.perf_counter()

for i in range(nsamples):
   st = time.perf_counter()
   indata[i] = vin.voltage
   while (time.perf_counter() - st) <= sinterval:
      pass

t = time.perf_counter() - t0

xpoints = np.arange(0, ACQTIME, sinterval)

print('Time elapsed: %.9f s.' % t)
print()

f1, ax1 = plt.subplots()

#
# Default plotting style connects points with lines
#
ax1.plot(xpoints, indata)
ax1.set_title("Solarcell voltages over time")
ax1.set_ylabel("Voltages (Volts)")
ax1.set_xlabel("Time (seconds)")
#
# Plotting with steps is better for visualizing sampling
#
# ax1.plot(xpoints, indata,'-',drawstyle='steps-post')

f1.show()

input("\nPress <Enter> to exit...\n")
