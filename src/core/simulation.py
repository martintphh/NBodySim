import numpy as np
from .body import Body
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # aktiviert 3D-Plotting
from matplotlib.animation import FuncAnimation
from .energy import *


def compute_all_forces(bodies):
    """Compute net gravitational forces on each body from all others."""

    forces = [np.zeros(3) for _ in bodies]
    for i, body_i in enumerate(bodies):
        for j, body_j in enumerate(bodies):
            if j != i:
                forces[i] += body_i.force_from(body_j)
    return forces

def euler_update(bodies, forces, dt):
    """Update velocities and positions using the Euler method."""
    for body, force in zip(bodies, forces):
        acceleration = force / body.mass
        body.velocity += acceleration * dt
        body.position += body.velocity * dt

def simulate(bodies, steps, dt):
    """
    Simulate the N-body system using Euler integration.
    
    Returns:
        positions (List[List[np.ndarray]]): Positions of each body over time.
        kinetic_energy (List[float])
        potential_energy (List[float])
        time (List[float])
    """
    positions = [[] for body in bodies]
    T = []
    V = []
    time = []
    t = 0.
    for _ in range(steps):
        forces = compute_all_forces(bodies)
        euler_update(bodies, forces, dt)
        for i, body in enumerate(bodies):
            positions[i].append(body.position.copy())
        T.append(calculate_kinetic_energy(bodies))
        V.append(calculate_potential_energy(bodies))
        time.append(t)
        t += dt
        
    return positions, T, V, time
