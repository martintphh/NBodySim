import numpy as np
import matplotlib.pyplot as plt

def calculate_kinetic_energy(bodies):
    energies = []
    for body in bodies:
        energy = body.mass * np.dot(body.velocity, body.velocity) / 2
        energies.append(energy)
    return sum(energies)

def pot_energy(body_a, body_b, G):
    distance = np.linalg.norm(body_a.position - body_b.position)
    return - G * body_a.mass * body_b.mass / distance

def calculate_potential_energy(bodies, G = 6.6743e-11):
    potential_energies = []
    for i, body in enumerate(bodies):
        energy = 0.
        for j in range(len(bodies)):
            if j > i:
                energy += pot_energy(body,bodies[j], G)
        potential_energies.append(energy)
    return sum(potential_energies)


def energy(T, V):
    """takes in lists of kin energy an pot energy and returns arrays of T, V and E=T+V"""
    T, V = np.array(T), np.array(V)
    E = T + V
    return T, V, E

def energy_plot(T, V, E, time):
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(time, T, label="Kinetic Energy")
    ax.plot(time, E, label="Total Energy")
    ax.plot(time, V, label="Potential Energy")
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("Energy (J)")
    
    plt.tight_layout()
    plt.show()
    

            
