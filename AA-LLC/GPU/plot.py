import  matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

G1 = np.loadtxt('G1/benchmarks.dat')
G2 = np.loadtxt('G2/benchmarks.dat')
G4 = np.loadtxt('G4/benchmarks.dat')
G8 = np.loadtxt('G8/benchmarks.dat')

print('G1:\n', G1)
print('G2:\n', G2)
print('G4:\n', G4)
print('G8:\n', G8, '\n\n')

plt.rc('font' , size =12)
plt.ylabel('performance (ns/day)')
plt.xlabel('GPUs')
plt.title('AA simulation on GPU nodes')
# plt.xscale("log")
# plt.yscale("log")
plt.xticks([1,2,4,8])

data = np.zeros((4,2))
data[0,:] = G1[3,:]
data[1,:] = G2[2,:]
data[2,:] = G4[3,:]
data[3,:] = G8[3,:]
data[:,0] = data[:,0] / 5

plt.plot(data[:,0], data[:,1], marker='o', linewidth=2)

x = data[:-1,0]
y = data[:-1,1]
reg = linregress(x, y)
print('Fitting a line:\n\tx: {}\n\ty: {}'.format(x, y))

x = np.arange(1,8,step=1)
y = reg.slope*x + reg.intercept
plt.plot(x,y,ls='dashed',c='k')

plt.savefig('AA-LLC-gpus.png')

plt.show()
exit()

data =  np.loadtxt('benchmarks.dat')

plt.title('AA simulation on Bridges2 GPU nodes')
plt.rc('font' , size =12)
plt.ylabel('Performance (ns/day)')
plt.xlabel('GPUs')
#plt.xscale("log")
#plt.yscale("log")

x=data[:,0]
ymax=np.amax(data[:,1:],axis=1)

coef = np.polyfit(x[:2],ymax[:2],1)
fn =  np.poly1d(coef)



plt.xticks([1,2,4,8])
plt.plot(x, ymax,marker='o',  linewidth=2, label='best')

x0=np.linspace(1,4,4)
plt.plot(x0,fn(x0), '--k')

plt.savefig('AA-LLC-gpus.png')
plt.show()
plt.close()


exit()



