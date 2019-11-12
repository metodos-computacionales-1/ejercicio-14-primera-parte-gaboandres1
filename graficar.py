import numpy as np
import matplotlib.pyplot as plt

plt.figure()
data = np.loadtxt('data.dat')
plt.plot(data[:,0],data[:,1],label='velocidad')
plt.plot(data[:,0],data[:,2],label='posición')
plt.xlabel('t')
plt.legend()
plt.savefig('grafica.png')

plt.figure()
plt.plot(data[:,1],data[:,2])
plt.xlabel('v')
plt.ylabel('x')
plt.savefig('fase.png')
