from core.planets import *
from core.simulation import runge_kutta_update, euler_update
import os
# --- Simulation Parameters ---

# Time step in seconds (1 day)
dt = 24 * 60 * 60           # [s]

# Number of steps (e.g. 365 for one year)
steps = 365 *5

# Select bodies to simulate
bodies = [sun, mercury, venus, earth, mars]

# Choose integration method
# Either: runge_kutta_update or euler_update
integrator = runge_kutta_update

# --- File Naming (auto-generated) ---

# Human-readable method name for filenames
if integrator == runge_kutta_update:
    method = "rk4"
elif integrator == euler_update:
    method = "euler"
else:
    raise ValueError("Unknown integrator function.")

# Compute duration in years (assuming 365 steps = 1 year)
duration_years = steps / 365

# src/config → src
SRC_DIR = os.path.dirname(os.path.dirname(__file__))

# Projektordner = eine Ebene über src/
BASE_DIR = os.path.dirname(SRC_DIR)

# Pfad zum "results/"-Ordner auf gleicher Ebene wie src/
RESULTS_DIR = os.path.join(BASE_DIR, "results")

# Ordner anlegen, falls er noch nicht existiert
os.makedirs(RESULTS_DIR, exist_ok=True)

#File names for plots and animations
save_plot = os.path.join(RESULTS_DIR, f"plot_{len(bodies)}bodies_{int(duration_years)}y_{method}.png")
save_animation = os.path.join(RESULTS_DIR, f"animation_{len(bodies)}bodies_{int(duration_years)}y_{method}.mp4")
