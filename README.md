# DoublePendulumBars
Code to simulate the dynamics of a double pendulum subjected to an external moment, having a spring between bars and two dampers. 

## Problem 

A double pendulum consisting of two bars with masses $m_{1}$ and $m_{2}$, has an external moment applied to the first bar, and has losses at the joints, here represented with the damping coefficients $c_{1}$ and $c_{2}$. Also it has a torsional spring at the hinge between the two bars.  

![figura_barras_thetas_moment_damper_spring](https://github.com/user-attachments/assets/648a997d-b9a3-43ed-847e-91d5ce13d22e)

The dynamic of this system is given by two ODEs

$$J _{a} \ddot{\theta} _{1} + J _{x} \cos{(\theta _{1}-\theta _{2})}\ddot{\theta _{2}} +J _{x} \sin{(\theta _{1} - \theta _{2})} \dot{\theta}^{2} _{2}+\mu _{1} \sin{\theta _{1}} - k _{t}(\theta _{2} - \theta _{1}) =M(t)-c _{1}\dot{\theta} _{1}$$

$$m _{2} l _{2} \ddot{\theta} _{1} +m _{2} l _{1} \[\ddot{\theta} _{1} cos{(\theta _{1}-\theta _{2})}-\dot{\theta}^{2} _{1} \sin{(\theta _{1}-\theta _{2})}\]+ m _{2} g\sin{\theta _{2}}=0$$
