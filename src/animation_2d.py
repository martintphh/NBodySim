import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from simulation import *

def seconds_to_ddhh_single(second):
    dd = second // (3600 * 24)
    hh = (second % (3600 * 24)) // 3600
    return f"{int(dd):02d}days {int(hh):02d}hours"

def plot_2d(bodies, positions, time):
    fig = plt.figure(figsize=(12.5,7.5))
    ax = fig.add_subplot(111)

    for body, body_position in zip(bodies, positions):
        x = [pos[0] for pos in body_position]
        y = [pos[1] for pos in body_position]

        ax.plot(x,y, linestyle="-", label=body.name, )
        ax.scatter(x[-1], y[-1], s=30)

    #time_ddhh = seconds_to_ddhh_single(time)  
     
    #ax.text(0.05, 0.95, f't = {time_ddhh[-1]}', 
    #    horizontalalignment='left',
    #    verticalalignment='top',
    #    transform=ax.transAxes)

    ax.set_aspect('equal')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('2D Bahnen der Körper')
    ax.legend()
    plt.tight_layout()
    plt.show()


def animate_2d(bodies, positions, time):
    fig = plt.figure(figsize=(12.,7.5))
    ax = fig.add_subplot(111)
    
    all_x = [pos[0] for body_pos in positions for pos in body_pos]
    all_y = [pos[1] for body_pos in positions for pos in body_pos]

    margin = 0.1 * max(max(all_x) - min(all_x), max(all_y) - min(all_y))

    ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
    ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
    
    ax.set_title(f"2D Animation of {len(bodies)}-Body-Problem")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
        
    points = [ax.plot([],[], marker="o", label=body.name)[0] for body in bodies]
    trails = [ax.plot([],[], "-",linewidth=0.5)[0] for body in bodies]
    ax.set_aspect('equal')
    ax.legend()

    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    def update(frame):
        for i, body in enumerate(bodies):
            pos = positions[i][frame]
            points[i].set_data(pos[0], pos[1])

            x_trail = [p[0] for p in positions[i][:frame+1]]
            y_trail = [p[1] for p in positions[i][:frame+1]]
            trails[i].set_data(x_trail, y_trail)

        time_text.set_text(f"t = {seconds_to_ddhh_single(time[frame])}")
        return points + trails + [time_text]


    ani = FuncAnimation(fig=fig, func=update, frames=len(time), interval=10)
    plt.tight_layout()
    plt.show()