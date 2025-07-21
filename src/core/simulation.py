import numpy as np
from .body import Body
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from .energy import *


def compute_all_forces(bodies):
    """Compute net gravitational forces on each body from all others."""

    forces = [np.zeros(3) for _ in bodies]
    for i, body_i in enumerate(bodies):
        for j, body_j in enumerate(bodies):
            if j != i:
                f = body_i.force_from(body_j)
                forces[i] += f

    return forces

def euler_update(bodies, dt):
    """Update velocities and positions using the Euler method."""
    forces=compute_all_forces(bodies)
    for body, force in zip(bodies, forces):
        acceleration = force / body.mass
        body.velocity += acceleration * dt
        body.position += body.velocity * dt


def runge_kutta_update(bodies, dt):
    """Update velocities and positions using Runge-Kutta method."""
    N = len(bodies)
    # Hilfsfunktionen
    def get_positions():
        return np.array([body.position for body in bodies])

    def get_velocities():
        return np.array([body.velocity for body in bodies])

    def set_positions(pos_array):
        for i, body in enumerate(bodies):
            body.position = pos_array[i]

    def set_velocities(vel_array):
        for i, body in enumerate(bodies):
            body.velocity = vel_array[i]

    # Kräfte berechnen (Beschleunigungen)
    def accelerations(pos_array, vel_array):
        # Dummy bodies mit aktuellen pos/vel
        for i, body in enumerate(bodies):
            body.position = pos_array[i]
            body.velocity = vel_array[i]
        forces = compute_all_forces(bodies)
        acc = np.array([f / body.mass for f, body in zip(forces, bodies)])
        return acc

    r0 = get_positions()
    v0 = get_velocities()
    a0 = accelerations(r0, v0)

    k1_r = v0
    k1_v = a0

    k2_r = v0 + 0.5 * dt * k1_v
    k2_v = accelerations(r0 + 0.5 * dt * k1_r, k2_r)

    k3_r = v0 + 0.5 * dt * k2_v
    k3_v = accelerations(r0 + 0.5 * dt * k2_r, k3_r)

    k4_r = v0 + dt * k3_v
    k4_v = accelerations(r0 + dt * k3_r, k4_r)

    r_new = r0 + (dt / 6) * (k1_r + 2*k2_r + 2*k3_r + k4_r)
    v_new = v0 + (dt / 6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)

    set_positions(r_new)
    set_velocities(v_new)


        

def simulate(bodies, steps, dt, integrator=runge_kutta_update):
    """
    Simulate the N-body system using Euler integration.
    
    Returns:
        positions (List[List[np.ndarray]]): Positions of each body over time.
        kinetic_energy (List[float])
        potential_energy (List[float])
        time (List[float])
    """
    positions = [[] for body in bodies]
    T, V, time = [], [], []
    t = 0.
    for _ in range(steps):
        integrator(bodies, dt)
        for i, body in enumerate(bodies):
            positions[i].append(body.position.copy())
        T.append(calculate_kinetic_energy(bodies))
        V.append(calculate_potential_energy(bodies))
        time.append(t)
        t += dt
        
    return positions, T, V, time
