import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

## Double Pendulum System 

###########################################################################################################
# Coded by Juan Andrés Santisteban Hidalgo, PhD
###########################################################################################################
############### Parameters ################################################################################

L1 = 1   # length of bar 1 [m]
L2 = 1   # length of bar 2 [m]
m1 = 1   # mass 1 [kg]
m2 = 1   # mass 2 [kg]
g = 9.81 # gravity [m/s^2]
kt = 0.1   # torsional spring constant [Nm/rad]
c1 = 0.01  # damping constant of bar 1 [Nms/rad]
c2 = 0.01  # damping constant of bar 2 [Nms/rad]

mo = 1    # imposed moment amplitude [Nm]
Hz = 1.5  # frequency of imposed moment [Hz]

omega = Hz*2*np.pi              # forcing function angular frequency [rad/s]

Ja = (1/3)*m1*L1**2 + m2*L1**2
Jb = (1/3)*m2*L2**2
Jx = (1/2)*m2*L1*L2

mu1 = ((1/2)*m1+m2)*g*L1
mu2 = (1/2)*m2*g*L2

## Simulation time ########################################################################################
t0 = 0  # initial time [s]
tf = 10 # final time [s]
delta_t = 0.01                          # time step [s]
nt = int(np.round(tf/delta_t))          # number of time steps
tspan = np.linspace(t0, tf, nt)         # time span [s]

## Initial Conditions ######################################################################################
theta1 = 0        # initial angle of bar 1 [rad]
theta2 = np.pi/2        # initial angle of bar 2 [rad]
dtheta1 = 0             # initial angular velocity of bar 1 [rad/s]
dtheta2 = 0      # initial angular velocity of bar 2 [rad/s]

Y0 = [theta1, theta2, dtheta1, dtheta2]                       # initial conditions vector
###########################################################################################################
###########################################################################################################

def doublePendulum(t, y):

    n = 2
    M = np.array([[Ja, Jx*np.cos(y[0]-y[1])],[Jx*np.cos(y[0]-y[1]), Jb]])
    G = np.array([[0, Jx*y[3]*np.sin(y[0]-y[1])],[-Jx*y[2]*np.sin(y[0]-y[1]), 0]])
    A = np.block([[np.zeros((n,n)), np.eye(n)],[np.zeros((n,n)), -np.matmul(np.linalg.inv(M),G)]])
    B = np.block([[np.zeros((n,n))],[np.linalg.inv(M)]])
    F = np.array([-mu1*np.sin(y[0])+kt*(y[1]-y[0])+mo*np.sin(omega*t)-c1*y[2], -mu2*np.sin(y[1])-kt*(y[1]-y[0])-c2*(y[3]-y[2])])
    dy = np.matmul(A,y)+np.matmul(B,F)

    return np.transpose(dy)

Y = np.zeros((len(tspan), len(Y0)))   # array for solution
Y[0, :] = Y0

r = integrate.ode(doublePendulum).set_integrator("dopri5")  # choice of method
r.set_initial_value(Y0, tspan[0])   # initial values
for i in range(1, tspan.size):
   Y[i, :] = r.integrate(tspan[i]) # get one more value, add it to the array
   if not r.successful():
       raise RuntimeError("Could not integrate")

## Animation of the double pendulum
def pendulum_animation(T1, Y1):
    global L1, L2
    N = len(T1)

    plt.figure()
    for i in range(N):
        plt.plot([0, L1 * np.sin(Y1[i, 0])], [0, -L1 * np.cos(Y1[i, 0])], 'r', linewidth=2)
        plt.plot([L1 * np.sin(Y1[i, 0]), L1 * np.sin(Y1[i, 0]) + L2 * np.sin(Y1[i, 1])],
                 [-L1 * np.cos(Y1[i, 0]), -L1 * np.cos(Y1[i, 0]) - L2 * np.cos(Y1[i, 1])], 'r', linewidth=2)
        plt.xlim([-(L1 + L2), (L1 + L2)])
        plt.ylim([-(L1 + L2), 0])
        plt.pause(0.05)
        plt.clf()

pendulum_animation(tspan,Y)

# plot of the dynamic response of bar 1
fig, ax = plt.subplots()
plt.plot(tspan, Y[:,0],'r')
ax.set_title('Dynamic Response of Bar 1')
ax.set_xlabel('t [s]')
ax.set_ylabel('x(t) [m]')
ax.grid()
ax.set_axisbelow(True)

# plot of the phase diagram of bar 1
fig, ax = plt.subplots()
plt.plot(Y[:,0], Y[:,2], 'g')
ax.set_title('Phase Diagram of Bar 1')
ax.set_xlabel('x(t) [m]')
ax.set_ylabel('xdot(t) [m/s]')
ax.grid()
ax.set_axisbelow(True)

# plot of the dynamic response of bar 2
fig, ax = plt.subplots()
plt.plot(tspan, Y[:,1],'r')
ax.set_title('Dynamic Response of Bar 2')
ax.set_xlabel('t [s]')
ax.set_ylabel('x(t) [m]')
ax.grid()
ax.set_axisbelow(True)

# plot of the phase diagram of bar 2
fig, ax = plt.subplots()
plt.plot(Y[:,1], Y[:,3], 'g')
ax.set_title('Phase Diagram of Bar 2')
ax.set_xlabel('x(t) [m]')
ax.set_ylabel('xdot(t) [m/s]')
ax.grid()
ax.set_axisbelow(True)

plt.show()
