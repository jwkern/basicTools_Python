import numpy as np
import matplotlib.pyplot as plot

plot.scatter(*np.loadtxt("cmd.txt",unpack=True), linewidth=2.0)
plot.scatter(*np.loadtxt("cmd_shifted.txt",unpack=True), linewidth=2.0)

plot.xlabel('B-V')
plot.xlim(-1, 2)
plot.ylim(16, 7)
plot.ylabel('Apparent V Magnitude')
plot.title('Color-Magnitude Diagram for NGC 884')
plot.show()
