import numpy as np
import seaborn as sns
sns.set_theme(style="darkgrid")
from core.body import Body
from core.simulation import *
import matplotlib.pyplot as plt
from core.planets import *
from core.energy import combine_energies, energy_plot
from visualization.animation_2d import animate_2d, plot_2d
from config import config
from core.perihel_rotation import find_perihels

import logging
logging.basicConfig(level=logging.INFO)

def main():

    dt = config.dt
    steps = config.steps
    bodies = config.bodies
    integrator = config.integrator
    save_plot = config.save_plot
    save_animation = config.save_animation
    save_energy = config.save_energy

    positions, T, V, time = simulate(bodies, steps, dt, integrator=integrator) #rk4 simulation

    positions_2d = [[[x, y] for x, y, _ in body_pos] for body_pos in positions]

    # 2D Plot speichern
    plot_2d(bodies, positions_2d, time, save_path=save_plot)
    plt.close()

    # Animation speichern als GIF oder MP4
    animate_2d(bodies, positions_2d, time, save_path=save_animation)

    # Berechnung der Gesamtenergie (kinetisch + potenziell)
    T, V, E = combine_energies(T, V)

    # Optional: Energieverlauf plotten 
    energy_plot(T, V, E, time, save_energy)                       
    
    """find_perihels(positions_2d, bodies, "Mercury", time)"""   #experimental function to calculate perihel rotation


    logging.info("Simulation completed.")
    logging.info(f"Plot saved to {save_plot}")
    logging.info(f"Animation saved to {save_animation}")
    
    return 0


if __name__ == "__main__":
    main()
