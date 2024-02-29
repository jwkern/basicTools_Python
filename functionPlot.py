import matplotlib.pyplot as plt
import math
import numpy as np
import pylab

a=np.linspace(1e-5,1,1000)

rad = 1e-4/a**4
mat = 0.3/a**3
dar = 0.7*a/a


plt.plot(a,rad,'r')
plt.plot(a,mat,'b')
plt.plot(a,dar,'g')
plt.xscale('log')
plt.yscale('log')
#plt.legend ()
plt.xlabel('Scale Factor')
plt.ylabel('Normalized Energy Density')
#plt.title()
#plt.xlim ()
#plt.ylim ()
plt.show()
