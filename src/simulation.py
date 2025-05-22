import numpy as np
from body import Body
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # aktiviert 3D-Plotting
from matplotlib.animation import FuncAnimation


def compute_all_forces(bodies):
    """Berechnet die Gesamtkraft auf einen Körper durch alle anderen gemäß Newton Gravitationsgesetz
    returns forces (list)"""

    forces = [np.zeros(3) for _ in bodies]
    for i, body_i in enumerate(bodies):
        for j, body_j in enumerate(bodies):
            if j != i:
                forces[i] += body_i.force_from(body_j)
    return forces

def euler_update(bodies, forces, dt):
    """updated die Geschwindigkeiten und Positionen gemäß Euler-Methode"""
    for body, force in zip(bodies, forces):
        acceleration = force / body.mass
        body.velocity += acceleration * dt
        body.position += body.velocity * dt

def simulate(bodies, steps, dt):
    """führt die Simulation für Anzahl an Schritten durch und returns Liste an posistionen"""
    positions = [[] for body in bodies]
    for _ in range(steps):
        forces = compute_all_forces(bodies)
        euler_update(bodies, forces, dt)
        for i, body in enumerate(bodies):
            positions[i].append(body.position.copy())
    return positions


def plot_trajectories_3d(bodies, positions):
    """
    bodies: Liste von Body-Objekten (für Namen/Farben)
    positions: Liste von Listen mit Positionen (pro Körper über Zeit)
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for body, body_positions in zip(bodies, positions):
        # x, y, z-Koordinaten extrahieren
        x = [pos[0] for pos in body_positions]
        y = [pos[1] for pos in body_positions]
        z = [pos[2] for pos in body_positions]

        ax.plot(x, y, z, label=body.name)  # Bahnlinie
        ax.scatter(x[-1], y[-1], z[-1], s=20)  # aktuelle Position (Endpunkt)

    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    ax.set_title('3D Bahnen der Körper')
    ax.legend()
    plt.tight_layout()
    plt.show()


def animation(bodies, positions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    all_x = [pos[0] for body_pos in positions for pos in body_pos] #Achsen-Limits
    all_y = [pos[1] for body_pos in positions for pos in body_pos]
    all_z = [pos[2] for body_pos in positions for pos in body_pos]

    ax.set_xlim(min(all_x), max(all_x))
    ax.set_ylim(min(all_y), max(all_y))
    ax.set_zlim(min(all_z), max(all_z))
    ax.set_box_aspect([1,1,1])

    ax.set_title(f"3D Animation of {len(bodies)}-Problem")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("z (m)")

    points = [ax.plot([], [], [], "o", label=body.name)[0] for body in bodies]
    trails = [ax.plot([],[],[], "-",linewidth=0.5)[0] for body in bodies]
    ax.legend()

    def update(frame):
        for i, body in enumerate(bodies):
            pos = positions[i][frame]
            trail = positions[i][:frame+1]

            points[i].set_data(pos[0], pos[1])
            points[i].set_3d_properties(pos[2])
            
            x_trail = [p[0] for p in trail]
            y_trail = [p[1] for p in trail]
            z_trail = [p[2] for p in trail]
            trails[i].set_data(x_trail, y_trail)
            trails[i].set_3d_properties(z_trail)
        return points + trails

    ani = FuncAnimation(fig, update, frames=len(positions[0]), interval=10, blit=False)
    plt.tight_layout()
    plt.show()