import  matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

data =  np.loadtxt('benchmarks.dat')

plt.rc('font' , size =12)
plt.ylabel('performance (ns/day)')
plt.xlabel('processors')
plt.title('AA simulation on RM nodes')
# plt.xscale("log")
# plt.yscale("log")
plt.xticks([16,64,128,256,384])

plt.plot(data[:,0], data[:,1], marker='o', linewidth=2)

x = data[:7,0]
y = data[:7,1]
reg = linregress(x, y)
print('Fitting a line:\n\tx: {}\n\ty: {}'.format(x, y))

x = np.arange(0,384,step=1)
y = reg.slope*x + reg.intercept
plt.plot(x,y,ls='dashed',c='k')

plt.savefig('AA-PA-cores.png')

plt.show()
exit()



