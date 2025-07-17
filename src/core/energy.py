import numpy as np
import matplotlib.pyplot as plt

def calculate_kinetic_energy(bodies):
    """
    Computes the total kinetic energy of all bodies.

    Parameters:
    - bodies: list of Body instances

    Returns:
    - total kinetic energy (float)
    """
    energies = []
    for body in bodies:
        #T=(1/2)*m*v^2
        energy = body.mass * np.dot(body.velocity, body.velocity) / 2
        energies.append(energy)
    return sum(energies)

def pot_energy(body_a, body_b, G):
    """
    Computes the gravitational potential energy between two bodies.

    Parameters:
    - body_a: first Body instance
    - body_b: second Body instance
    - G: gravitational constant

    Returns:
    - potential energy (float)
    """
    distance = np.linalg.norm(body_a.position - body_b.position)
    return - G * body_a.mass * body_b.mass / distance

def calculate_potential_energy(bodies, G = 6.6743e-11):
    """
    Computes the total gravitational potential energy for all pairs of bodies.

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

def energy_plot(T, V, E, time):
    """
    Plots kinetic, potential, and total energy over time.

    Parameters:
    - T: kinetic energy array
    - V: potential energy array
    - E: total energy array
    - time: array of time values (same length as T, V, E)
    """
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(time, T, label="Kinetic Energy")
    ax.plot(time, E, label="Total Energy")
    ax.plot(time, V, label="Potential Energy")
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("Energy (J)")
    
    plt.tight_layout()
    plt.show()
    

            
