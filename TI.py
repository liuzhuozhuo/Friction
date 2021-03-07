import numpy as np
import matplotlib.pyplot as plt

#define initial conditions
h1=33.5
h2=43.5
h3=53.5
v0x=270
v0y=0
x0=0
g=980
b=0.35

t1 = np.linspace(0, 0.265, 1000)
t2 = np.linspace(0, 0.300, 1000)
t3 = np.linspace(0, 0.332, 1000)

#calculate x
def eqforx (t):
    x=x0+v0x*t
    return x
def xposition (t):
    x=(v0x/b)*(1-np.exp(-b*t))
    return x

#calculate y
def eqfory1 (t1):
    y=h1+v0y*t1-(g*t1**2)/2
    return y
def eqfory2 (t2):
    y=h2+v0y*t2-(g*t2**2)/2
    return y
def eqfory3 (t3):
    y=h3+v0y*t3-(g*t3**2)/2
    return y
def yposition1 (t):
    y=h1+(1/b)*((g/b)+v0y)*(1-np.exp(-b*t))-(g/b)*t
    return y
def yposition2 (t):
    y=h2+(1/b)*((g/b)+v0y)*(1-np.exp(-b*t))-(g/b)*t
    return y
def yposition3 (t):
    y=h3+(1/b)*((g/b)+v0y)*(1-np.exp(-b*t))-(g/b)*t
    return y

#Ideal
x1=[eqforx(s)for s in t1]
x2=[eqforx(s)for s in t2]
x3=[eqforx(s)for s in t3]
y1=[eqfory1(s)for s in t1]
y2=[eqfory2(s)for s in t2]
y3=[eqfory3(s)for s in t3]

#With resistense
xf1 = [xposition(s) for s in t1]
xf2 = [xposition(s) for s in t2]
xf3 = [xposition(s) for s in t3]
yf1= [yposition1(s) for s in t1]
yf2= [yposition2(s) for s in t2]
yf3= [yposition3(s) for s in t3]

#real
xr1=[0,20,40,60,67]
xr2=[0,20,40,60,78]
xr3=[0,20,40,60,80,86]

yr1=[33.5,31,23,7,0]
yr2=[43.5,42,34,20,0]
yr3=[53.5,50,42,30,10,0]

angulo= 0

fig=plt.figure(figsize=(7,5))
ax=fig.add_subplot(111)
ax.plot (x1,y1, color="green",label="Ideal 30m")
ax.plot (x2,y2, color="blue",label="Ideal 40m")
ax.plot (x3,y3, color="tab:red",label="Ideal 50m")
ax.plot (xr1,yr1, color="green",linestyle='--',label="Real 30m")
ax.plot (xr2,yr2, color="blue",linestyle='--',label="Real 40m")
ax.plot (xr3,yr3, color="tab:red",linestyle='--',label="Real 50m")
ax.plot (xf1,yf1, color="green",linestyle=':',label="Friction 30m")
ax.plot (xf2,yf2, color="blue",linestyle=':',label="Friction 40m")
ax.plot (xf3,yf3, color="tab:red",linestyle=':',label="Friction 50m")

ax.set_xlabel("x-coordinate",fontsize=12)
ax.set_ylabel("y-coordinate",fontsize=12)
ax.legend(loc="upper right",fontsize=12)