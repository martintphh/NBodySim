import numpy as np
import seaborn as sns
sns.set_theme(style="darkgrid")
from core.body import Body
from core.simulation import simulate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # für 3D-Plotting, falls benötigt
from core.planets import earth, sun, mercury, venus, mars  # gezielt importieren, was du nutzt
from core.energy import combine_energies, energy_plot
from visualization.animation_2d import animate_2d, plot_2d


def main():

    bodies = [earth, sun, mercury, venus, mars]

    dt = 1 * 60 * 60  # 1 Stunde in Sekunden
    steps = 12 * 365 * 24  # ca. 1 Jahr

    positions, T, V, time = simulate(bodies, steps, dt)
    positions_2d = [[[x, y] for x, y, _ in body_pos] for body_pos in positions]

    # 2D Plot speichern
    plot_2d(bodies, positions_2d, time)
    plt.savefig("trajectories_2d.png", dpi=300)
    plt.close()

    # Animation speichern als GIF oder MP4
    animate_2d(bodies, positions_2d, time, save_path="nbody_simulation.gif")

    # Berechnung der Gesamtenergie (kinetisch + potenziell)
    T, V, E = combine_energies(T, V)

    # Optional: Energieverlauf plotten (aktuell auskommentiert)
    # energy_plot(T, V, E, time)

    return 0


if __name__ == "__main__":
    main()
