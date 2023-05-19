from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

FTIME = 60      # function range in seconds
FS = 4       # samples per second
npts = FTIME*FS  # number of sample points

def exp(x,A,t):
    y = A*np.exp(-1*t*x) + C
    return y

file = open('p6_hw7_data.txt')
data = np.loadtxt(file)
file.close()
C = data[0]
print(C)
yvals = data[25:]
xvals = np.linspace(0, FTIME, npts-25)

parameter, covariance = curve_fit(exp,xvals,yvals )

constant = parameter[1]
print("The time constant is : %s" % constant)


#printing curves
f1, ax1 = plt.subplots()


ax1.plot(xvals, yvals)
ax1.plot(xvals, exp(xvals,parameter[0],parameter[1]))
plt.legend(["data points","fitted function"])
ax1.set_title("Cooling Curve of MCP9808")
ax1.set_ylabel("Temperature (C)")
ax1.set_xlabel("Time (seconds)")
#


f1.show()

input("\nPress <Enter> to exit...\n")