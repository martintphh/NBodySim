import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def find_perihels(positions: list, bodies: list, body_name: str, time: list):
    bodies_dict = {body.name: idx for idx, body in enumerate(bodies)}


    positions_sun = positions[bodies_dict["Sun"]]
    position_body = positions[bodies_dict[body_name]]
    print(np.array(position_body).shape)
    print(np.array(positions_sun).shape)
    r_vec = np.array(position_body) - np.array(positions_sun)
    
    r = np.linalg.norm(r_vec, axis=1)


    minima_indices, _ = sp.signal.find_peaks(-r)
    minima_indices = np.sort(minima_indices)


    x_i, y_i = r_vec[minima_indices, 0], r_vec[minima_indices, 1]

    t_i = np.array(time)[minima_indices]
    theta_i = np.arctan2(y_i, x_i)

    t_days = t_i / (3600*24)
    t_years = np.array(time)[minima_indices] / (3600 * 24 * 365.25)

    theta_unwrapped = np.unwrap(theta_i)  # unwrap in radians
    theta_unwrapped_deg = np.degrees(theta_unwrapped)

    slope, intercept = np.polyfit(t_years, theta_unwrapped, deg=1)

    window_size = 5
    theta_smoothed = np.convolve(theta_unwrapped_deg, np.ones(window_size)/window_size, mode='valid')
    t_smoothed = t_years[(window_size-1)//2 : -(window_size//2)]

    plt.scatter(t_smoothed, theta_smoothed)
    #plt.plot(t_years, slope * np.array(t_years) + intercept, 'r-', label=f'Fit: {slope:.4f} °/Jahr')
    plt.xlabel("Time (y)")
    plt.ylabel("Perihel (degree)")
    #plt.title("Periheldrehung mit entrolltem Winkel")
    plt.savefig("perihel.png", dpi=300)
    plt.show()