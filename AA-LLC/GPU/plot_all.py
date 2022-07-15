import  matplotlib.pyplot as plt
import numpy as np


G1 = np.loadtxt('G1/benchmarks.dat')
G2 = np.loadtxt('G2/benchmarks.dat')
G4 = np.loadtxt('G4/benchmarks.dat')
G8 = np.loadtxt('G8/benchmarks.dat')

plt.rc('font' , size =12)
plt.ylabel('performance (ns/day)')
plt.xlabel('processors')

plt.plot(G1[:,0], G1[:,1], marker='o', label='1 GPU')
plt.plot(G2[:,0], G2[:,1], marker='o', label='2 GPUs')
plt.plot(G4[:,0], G4[:,1], marker='o', label='4 GPUs')
plt.plot(G8[:,0], G8[:,1], marker='o', label='8 GPUs')

plt.legend()
plt.savefig('test_GPU.png')
plt.show()
plt.close()

exit()



