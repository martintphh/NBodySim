import numpy as np
import matplotlib.pyplot as plt

AU = 1.497e11 # 1AU in m

def calculate_kinetic_energy(bodies):
    """
    Computes the total kinetic energy of all bodies (in Joule).

    Parameters:
    - bodies: list of Body instances

    Returns:
    - total kinetic energy (float)
    """
    energies = []
    for body in bodies:
        #T=(1/2)*m*v^2
        energy = body.mass * np.dot(body.velocity * AU, body.velocity * AU) / 2
        energies.append(energy)
    return sum(energies)

def pot_energy(body_a, body_b, G):
    """
    Computes the gravitational potential energy between two bodies (in Joule).

    Parameters:
    - body_a: first Body instance
    - body_b: second Body instance
    - G: gravitational constant

    Returns:
    - potential energy (float)
    """
    distance = np.linalg.norm(body_a.position - body_b.position)
    distance_in_meters = distance * AU

    return - G * body_a.mass * body_b.mass / distance_in_meters

def calculate_potential_energy(bodies, G = 6.6743e-11):
    """
    Computes the total gravitational potential energy for all pairs of bodies (in Joule).

    Parameters:
    - bodies: list of Body instances
    - G: gravitational constant (default: SI units)

    Returns:
    - total potential energy (float)
    """
    potential_energies = []
    for i, body in enumerate(bodies):
        energy = 0.
        for j in range(len(bodies)):
            if j > i:
                energy += pot_energy(body,bodies[j], G)
        potential_energies.append(energy)
    return sum(potential_energies)


def combine_energies(T, V):
    """
    Combines lists of kinetic and potential energy values to compute total energy.

    Parameters:
    - T: array-like, kinetic energy at each time step
    - V: array-like, potential energy at each time step

    Returns:
    - Tuple of arrays: (T, V, E) where E = T + V
    """
    T, V = np.array(T), np.array(V)
    E = T + V
    return T, V, E

def energy_plot(T, V, E, time, save_path):
    """
    Plots kinetic, potential, and total energy over time.

    Parameters:
    - T: kinetic energy array
    - V: potential energy array
    - E: total energy array
    - time: array of time values (same length as T, V, E)
    """    
    time = [t / (3600*24) for t in time]        #converting t(s) -> t(d)


    fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 6))
    axs[0].plot(time, T, label='Kinetic Energy T', color='tab:blue')
    axs[1].plot(time, V, label='Potential Energy V', color='tab:orange')
    axs[2].plot(time, E, label='Total Energy E = T + V', color='tab:green')

    ymin = min(np.min(T), np.min(V), np.min(E)) * 1.15
    ymax = max(np.max(T), np.max(V), np.max(E)) * 1.15
    for ax in axs:
        ax.set_ylim(ymin, ymax)

    axs[0].legend(loc='upper right')
    axs[1].legend(loc='upper right')
    axs[2].legend(loc='upper right')
    axs[2].set_xlabel("Time (d)")
    for ax in axs:
        ax.set_ylabel("Energy (J)")
    
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
    

            
