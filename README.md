# DoublePendulumBars
Code to simulate the dynamics of a double pendulum subjected to an external moment, having a spring between bars and two dampers. 

## Problem 

A double pendulum consisting of two bars with masses $m_{1}$ and $m_{2}$, has an external moment applied at the hinge of the first bar, and has losses at the joints, here represented with the damping coefficients $c_{1}$ and $c_{2}$. Also it has a torsional spring $k_{t}$ at the hinge between the two bars. 

![figura_barras_thetas_moment_damper_spring](https://github.com/user-attachments/assets/648a997d-b9a3-43ed-847e-91d5ce13d22e)

The dynamic of this system is given by two ODEs

$$J _{a} \ddot{\theta} _{1} + J _{x} \cos{(\theta _{1}-\theta _{2})}\ddot{\theta} _{2} +J _{x} \sin{(\theta _{1} - \theta _{2})} \dot{\theta}^{2} _{2}+\mu _{1} \sin{\theta _{1}} - k _{t}(\theta _{2} - \theta _{1}) =M(t)-c _{1}\dot{\theta} _{1}$$

$$J_{x} \cos{(\theta _{1} - \theta _{2})} \ddot{\theta} _{1} + J _{b} \ddot{\theta} _{2} - J _{x}  \sin{(\theta _{1} - \theta _{2})} \dot{\theta}^{2} _{1} + \mu _{2} \sin{\theta _{2}} + k _{t} (\theta _{2} - \theta _{1})= -c _{2} (\dot{\theta} _{2} - \dot{\theta} _{1})$$

Where 

$$J _{a} = \frac{1}{3}m _{1} L^{2} _{1} + m _{2} L^{2} _{1} \\ 
J _{b} = \frac{1}{3} m _{2} L^{2} _{2} \\ 
J _{x} m _{2} L _{1} L _{2}$$

Giving the parameters and the appropriate initial conditions, we get the animation, the dynamic plots, and the phase diagrams!

![DoublePendulumBarsAnimation](https://github.com/user-attachments/assets/375e783c-92bd-4b3f-9ee7-4f85eb74efbe)


![DoublePendulumDynamicResponseBar1](https://github.com/user-attachments/assets/f55d0820-58f2-47e4-82f9-7691dfae79db)
![DoublePendulumPhaseDiagramBar1](https://github.com/user-attachments/assets/70c10730-8685-41be-813a-94711e143a2d)
![DoublePendulumDynamicResponseBar2](https://github.com/user-attachments/assets/834715eb-b894-4831-94d3-404245fb36bf)
![DoublePendulumPhaseDiagramBar2](https://github.com/user-attachments/assets/8efab99d-c12b-4a9e-9483-4ca2771df4a5)

## Input Parameters

$m_{1}$ - mass of bar 1 [kg]

$m_{2}$ - mass of bar 2 [kg]

$L_{1}$ - length of bar 1 [m]

$L_{2}$ - length of bar 2 [m]

$g$ - gravity [m/s²]

$k_{t}$ - torsional spring constant [Nm/rad]

$c_{1}$ - damping constant of bar 1 [Nms/rad]

$c_{2}$ - damping constant of bar 2 [Nms/rad]

$mo$ - imposed moment amplitude [Nm]

$Hz$ - imposed moment frequency [Hz]

## Time of the simulation

$t_{0}$ - initial time [s]

$t_{f}$ - final time [s]

$\Delta t$ - timestep [s]

## Initial Conditions

$\theta_{1}^{0}$ - initial angle 1 [rad]

$\theta_{2}^{0}$ - initial angle 2 [rad]

$\dot{\theta}_{1}^{0}$ - initial angular velocity 1 [rad/s]

$\dot{\theta}_{2}^{0}$ - initial angular velocity 2 [rad/s]
