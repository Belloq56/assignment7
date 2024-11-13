import numpy as np
from matplotlib import pyplot as pp
from creategrid import qgrid

def r(x,xp,y,yp):
    return np.sqrt((x-xp)**2+(y-yp)**2)

def derx(x,xp,y,yp):
    return (x/np.sqrt((x-xp)**2+(y-yp)**2))

def dery(x,xp,y,yp):
    return (y/np.sqrt((x-xp)**2+(y-yp)**2))

charge=qgrid(50)
x=np.arange(-10,10,0.1)
y=np.arange(-20,20,0.1)
X,Y=np.meshgrid(x,y)

charges=[]
coord=[]
for i in charge['charges']:
    charges.append(i)
for i in charge['coordinates']:
    coord.append(i)
    
rows,cols=(400,200)
V=[[0]*cols]*rows
Ex1=[[0]*cols]*rows
Ey1=[[0]*cols]*rows
for i in range(len(charges)):
    Voltage = charges[i]/(4*np.pi*8.55e-12*r(X,coord[i][0],Y,coord[i][1]))
    V += Voltage
    Ex=-charges[i]/(4*np.pi*8.55e-12*derx(X,coord[i][0],Y,coord[i][1]))
    Ey=-charges[i]/(4*np.pi*8.55e-12*dery(X,coord[i][0],Y,coord[i][1]))
    Ex1 += Ex
    Ey1 += Ey
    
fig, (ax1) = pp.subplots(1)
cont1 = ax1.contourf(X,Y,V,levels=20)
fig.colorbar(cont1,ax=ax1,label='Voltage (V)')
ax1.set_xlabel('X (cm)')
ax1.set_ylabel('Y (cm)')

pp.quiver(X,Y,Ex1,Ey1)

pp.savefig('potential.png')