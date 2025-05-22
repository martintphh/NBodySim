import numpy as np
from body import Body
from simulation import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # aktiviert 3D-Plotting



def main():
    earth = Body(
        name="Earth",
        mass =5.972e24,
        position=np.array([1.496e11,0.,0.]),
        velocity=np.array([0.,29780.,0.]))

    sun = Body("Sun", 
    mass=1.9885e30,
    position=np.array([0,0,0]),
    velocity=np.array([0.,0.,0.]))
    
    jupyter = Body("Jupyter",
    mass=1.898e27,
    position=np.array([7.758e11,0,0]),
    velocity=np.array([0,13058,0]))


    bodies = [sun, earth, jupyter]

    dt = 60 * 60 *24 #1h in s
    steps = 365 * 24 #ein Jahr

    positions = simulate(bodies, steps, dt)
    
    #plot_trajectories_3d(bodies, positions)

    animation(bodies, positions)


    return 0

if __name__ == "__main__":
    main()