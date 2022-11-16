"""
Using fem1d.py to solve an Euler Bernoulli beam problem
"""
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from fem1d import EulerBernoulliBeam
#%% define beam
def f(x): # example loading
    if(x >=0 and x <= 1):
        return 8000 - 8000*x
    if(x>= 2 and x<= 4):
        return 8000
    return 0

EI = 3000000
b = lambda x: EI

beam = EulerBernoulliBeam(6, 6, f=f, b=b, title='Euler Bernoulli Beam, 6 elements')
beam.specify_dof(0, 0, 'w') # deflection left boundary condition
beam.specify_dof(0, 0, 'm') # moment left boundary condition
beam.specify_dof(0, 2, 'w')
beam.specify_dof(0, 4, 'w')
beam.specify_dof(0, 6, 'w') # deflection right boundary condition
beam.specify_dof(-2000, 6, 'm') # moment right boundary condition
#%% solve beam and plot all primary and secondary variables
beam.run()
x = beam.x
w = beam.w
theta = beam.theta
m = beam.m
v = beam.v 
# theta = beam.rotation
# m = beam.moment
# v = beam.shear_force
plt.close('all');
plt.figure(figsize=(6.5, 2.5))
plt.plot(x, w)
plt.xlabel('distance (m)')
plt.ylabel('deflection (m)')
plt.tight_layout()

plt.figure(figsize=(6.5,2.5))
plt.plot(x, theta)
plt.xlabel('distance (m)')
plt.ylabel('rotation')
plt.tight_layout()

plt.figure(figsize=(6.5,2.5))
plt.plot(x, m)
plt.xlabel('distance (m)')
plt.ylabel('moment (Nm)')
plt.tight_layout()

plt.figure(figsize=(6.5,2.5))
plt.plot(x, v)
plt.xlabel('distance (m)')
plt.ylabel('shear force (N)')
plt.tight_layout()