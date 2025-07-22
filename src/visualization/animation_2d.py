import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
 

def plot_2d(bodies, positions, time, save_path):
    fig = plt.figure(figsize=(12.5, 7.5))
    ax = fig.add_subplot(111)

    colors = plt.cm.tab10(np.linspace(0, 1, len(bodies)))

    for i, (body, body_positions) in enumerate(zip(bodies, positions)):
        x = [pos[0] for pos in body_positions]
        y = [pos[1] for pos in body_positions]

        ax.plot(x, y, linestyle="-", label=body.name, color=colors[i])
        ax.scatter(x[-1], y[-1], s=30, color=colors[i])

    num_bodies = len(bodies)
    ax.set_aspect('equal')
    ax.set_xlabel('x (AU)')
    ax.set_ylabel('y (AU)')
    ax.set_title(f'2D Trajectories of {num_bodies} Bodies')
    ax.legend()
    plt.tight_layout()

    plt.savefig(save_path, dpi=300)

    plt.show()


def seconds_to_ddhh_single(second):
    dd = second // (3600 * 24)
    hh = (second % (3600 * 24)) // 3600
    return f"{int(dd):02d}days {int(hh):02d}hours"

def animate_2d(bodies, positions, time, save_path):
    fig = plt.figure(figsize=(12, 7.5))
    ax = fig.add_subplot(111)

    all_x = [pos[0] for body_pos in positions for pos in body_pos]
    all_y = [pos[1] for body_pos in positions for pos in body_pos]

    if not all_x or not all_y:
        raise ValueError("Keine gültigen Positionsdaten für die Animation vorhanden.")

    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    max_range = max(max_x - min_x, max_y - min_y)
    margin = 0.1 * max_range if max_range > 0 else 1

    ax.set_xlim(min_x - margin, max_x + margin)
    ax.set_ylim(min_y - margin, max_y + margin)
    ax.set_aspect('equal')
    ax.set_title(f"2D Animation of {len(bodies)}-Body Problem")
    ax.set_xlabel("x (AU)")
    ax.set_ylabel("y (AU)")

    colors = plt.cm.tab10(np.linspace(0, 1, len(bodies)))
    points = [ax.plot([], [], marker="o", label=body.name, color=colors[i])[0] for i, body in enumerate(bodies)]
    trails = [ax.plot([], [], "-", linewidth=0.5, color=colors[i])[0] for i in range(len(bodies))]

    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
    ax.legend()

    def update(frame):
        for i in range(len(bodies)):
            pos = positions[i][frame]
            
            points[i].set_data([pos[0]], [pos[1]]) 

            x_trail = [p[0] for p in positions[i][:frame + 1]]
            y_trail = [p[1] for p in positions[i][:frame + 1]]
            trails[i].set_data(x_trail, y_trail)
            

        time_text.set_text(f"t = {seconds_to_ddhh_single(time[frame])}")
        return points + trails + [time_text]

    ani = FuncAnimation(fig=fig, func=update, frames=len(time), interval=10, blit=False)
    plt.tight_layout()
    ani.save(save_path, writer='pillow', fps=30)

    plt.show()

