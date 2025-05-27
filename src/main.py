import numpy as np
from body import Body
from simulation import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # aktiviert 3D-Plotting
from planets import *
from energy import *
from animation_2d import *


def main():
    bodies = [earth, sun, mercury, venus, jupiter, saturn, uranus, neptune, mars]
    #bodies = [earth, sun, mercury, venus, mars, jupiter, saturn, uranus, neptune]

    #for i in bodies:
     #   print(i)
    

    dt = 60 * 60  #1h in s
    steps = 12*365 * 24 #ein Jahr

    positions, T, V, time = simulate(bodies, steps, dt)
    positions_2d = [[[x,y] for x,y,_ in body_pos] for body_pos in positions]

    #print(np.array(positions_2d).shape)
    
    #print("x-Werte Körper 0:", [p[0] for p in positions_2d[0][:10]])
    #print("y-Werte Körper 0:", [p[1] for p in positions_2d[0][:10]])
    
    #plot_trajectories_3d(bodies, positions)
    plot_2d(bodies, positions, time)
    """animate_2d(bodies, positions_2d, time)"""
    
    #plot_trajectories_3d(bodies, positions)
    #animation(bodies, positions)
    
    #print(f"kinetische Energie Länge:{len(T)}")
    #print(f"potenitelle Energie Länge:{len(V)}")

    T, V, E = energy(T, V)
    #energy_plot(T, V, E, time)
    

    #print(np.array(positions).shape)
    return 0

if __name__ == "__main__":
    main()