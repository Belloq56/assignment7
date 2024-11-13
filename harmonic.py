import numpy as np
from matplotlib import pyplot as pp

def dy(V):
    return V

def dV(C,V,k,m,y):
    return -C*V-(k/m)*y

def euler1(x,y,h):
    return y + dy(x)*h

def euler2(C,V,k,m,y,h):
    return V + dV(C,V,k,m,y)*h

m=2
k=3
start=0
step=0.05
final=20
y=[2]
V=[0]
x=np.arange(start,final+step,step)


for i in range(len(x)-1):
    y.append(euler1(V[-1],y[-1],step))
    V.append(euler2((np.sqrt(4*k/m)),V[-1],k,m,y[-1],step))


pp.plot(x,V)
pp.show()
pp.savefig('harmonic.png')