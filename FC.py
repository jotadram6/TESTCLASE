#!/usr/bin/env python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


class sistema:
    def __init__(self, x, y, z, vx, vy, vz, ax, ay, az, m, q, t): #Funcion que se aplica sobre la classe misma (sel
        self.X = x
        self.Y = y
        self.Z = z
        self.VX = vx
        self.VY = vy
        self.VZ = vz
        self.AX = ax
        self.AY = ay
        self.AZ = az
        self.M = m
        self.q = q
        self.t=t
        
    def evolpos(self):
        self.X=self.X+self.VX*self.t+0.5*self.AX*(self.t*self.t)
        self.Y=self.Y+self.VY*self.t+0.5*self.AY*(self.t*self.t)
        self.Z=self.Z+self.VZ*self.t+0.5*self.AZ*(self.t*self.t)
        return self.X, self.Y, self.Z
   
    
    def evolvel(self):
        self.VX=self.VX+self.AX*self.t
        self.VY=self.VY+self.AY*self.t
        self.VZ=self.VZ+self.AZ*self.t
        return  self.VX, self.VY, self.VZ
    
    def acel(self,R0,R1,Q,B0=10,K=1):
        return (self.q*(self.VY*B0) + (self.q)*Q*(R0[0]-R1[0])/((R0[0]-R1[0])**2+(R0[1]-R1[1])**2+(R0[2]-R1[2])**2)**3/2)/self.M, (- self.q*(self.VX*B0) + (self.q)*Q*(R0[1]-R1[1])/((R0[0]-R1[0])**2+(R0[1]-R1[1])**2+(R0[2]-R1[2])**2)**3/2)/self.M, ((self.q)*Q*(R0[2]-R1[2])/((R0[0]-R1[0])**2+(R0[1]-R1[1])**2+(R0[2]-R1[2])**2)**3/2)/self.M 
    
        
        

Q1=sistema(0,0,0,0,0,0,0,0,0,10,1,0.01)
Q2=sistema(1,0,0,0,0,0,0,0,0,10,-1,0.01)
R0=Q1.evolpos();   R1=Q2.evolpos() 
V1=Q1.evolvel();   V2=Q2.evolvel()
A1=Q1.acel(R0,R1,1); A2=Q2.acel(R1,R0,-1)
i=0
N=10000
Datos1=np.zeros((9,N))
Datos2=np.zeros((9,N))
POSX=np.zeros()
while i<N-1:
    for j in range(0,3):
        Datos1[j][i]=R0[j]
        Datos2[j][i]=R1[j]
        Datos1[j+3][i]=V1[j]
        Datos2[j+3][i]=V2[j]
        Datos1[j+6][i]=A1[j]
        Datos2[j+6][i]=A2[j] 
        
        
        
        
    
    Q1=sistema(R0[0],R0[1],R0[2],V1[0],V1[1],V1[2],A1[0],A1[1],A1[2],10,1,0.01)
    Q2=sistema(R1[0],R1[1],R1[2],V2[0],V2[1],V2[2],A2[0],A2[1],A2[2],10,-1,0.01)
    R0=Q1.evolpos();   R1=Q2.evolpos() 
    V1=Q1.evolvel();    V1=Q2.evolvel()
    A1=Q1.acel(R0,R1,-1);  A2=Q2.acel(R1,R0,1)
    i=i+1

    #print("posicion 1",R0)
    #print("posicion 2",R1)
    #print("Velocidad 1",V1)
    #print("Velocidad 2",V1)
    #print("Aceleracion 1",A1)
    #print("Aceleracion 2",A2)
    
#Creamos grafica
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
x=Datos1[0]; y=Datos1[1]; z=Datos1[2]
x_=Datos2[0]; y_=Datos2[1]; z_=Datos2[2]
#
#ax.plot(x, y, z, label='parametric curve')
#ax.plot(x_, y_, z_, label='parametric curve')
#plt.ylim(-0.004,0.004)
plt.xlabel("x")
plt.ylabel("y")  
#plt.zlabel("z")  
ax.legend()
#Nombramos la puta esa
plt.show()

ax.scatter(x, y, z, c='g', marker='o')
ax.scatter(x_, y_, z_, c ='r', marker='o')
