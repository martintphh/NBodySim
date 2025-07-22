import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def find_perihels(positions: list, bodies: list, body_name: str, time: list):
    bodies_dict = {body.name: idx for idx, body in enumerate(bodies)}


    positions_sun = positions[bodies_dict["Sun"]]
    position_body = positions[bodies_dict[body_name]]

    r_vec = np.array(position_body) - np.array(positions_sun)
    
    r = np.linalg.norm(r_vec, axis=1)


    minima_indices, _ = sp.signal.find_peaks(-r)
    minima_indices = np.sort(minima_indices)


    x_i, y_i = r_vec[minima_indices, 0], r_vec[minima_indices, 1]

    t_i = np.array(time)[minima_indices]
    theta_i = np.arctan2(y_i, x_i)

    t_days = t_i / (3600*24)

    theta_unwrapped = np.unwrap(theta_i)  # theta_i sind deine Winkel aus arctan2

    theta_deg = np.degrees(theta_i)
    diffs = np.diff(theta_deg)
    diffs = (diffs + 180) % 360 - 180  # Winkel in (-180,180)
    theta_integrated = np.concatenate(([theta_deg[0]], theta_deg[0] + np.cumsum(diffs)))


    plt.scatter(theta_integrated, np.degrees(theta_unwrapped))
    plt.xlabel("Time (d)")
    plt.ylabel("Perihel (degree)")
    #plt.title("Periheldrehung mit entrolltem Winkel")
    plt.savefig("perihel.png", dpi=300)
