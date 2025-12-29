import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,101)
f=np.ones_like(x)
f[x<0]=-1
y1=(4/np.pi)*(np.sin(x)+np.sin(3*x)/3.0)
y2=y1+(4/np.pi)*(np.sin(5*x)/5.0+np.sin(7*x)/7.0)
y3=y2+(4/np.pi)*(np.sin(9*x)/9.0+np.sin(11*x)/11.0)

#plt.ion()
plt.plot(x,f,'b-',lw=3,label='f(x)')
plt.plot(x,y1,'c--',lw=2,label='two terms')
plt.plot(x,y2,'r-.',lw=2,label='four terms')
plt.plot(x, y3,'b:',lw=2,label='six terms')
plt.legend(loc='best')
plt.xlabel('x',style='italic')
plt.ylabel('partial sums',style='italic')
plt.suptitle('Partial sums for Fourier series of f(x)', size=10,weight='bold')
plt.savefig('RealisticPlot.png',dpi=300)
plt.show()
