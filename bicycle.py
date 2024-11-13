import numpy as np
from matplotlib import pyplot as pp

def f(P,m,v):
    return P/(m*v)

def euler(P,m,v,h):
    return v + f(P,m,v)*h

P=400
m=70
start=0
step=0.1
final=200
v=[4]
x=np.arange(start,final+step,step)


for i in range(len(x)-1):
    v.append(euler(P,m,v[-1],step))


pp.plot(x,v)
pp.show()
pp.savefig('bicycle.png')

