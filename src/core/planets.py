import numpy as np
import json
import os
from .body import Body

# Constants
AU = 1.497e11         # Astronomical Unit in meters
AU_per_d = 24 * 3600  # Seconds per day (used to convert velocity from AU/day to AU/s)

# Load planet data
filepath = os.path.join(os.path.dirname(__file__), "../config/planet_data.json")
with open(filepath, "r") as file:
    data = json.load(file)

# Helper function to create a Body from JSON data
def create_body(name, mass):
    return Body(
        name=name,
        mass=mass,
        position=np.array(data[name]["position"]),
        velocity=np.array(data[name]["velocity"]) / AU_per_d
    )

# Define all planets (and the Sun)
sun     = create_body("Sun",     1.9885e30)
mercury = create_body("Mercury", 3.285e23)
venus   = create_body("Venus",   4.867e24)
earth   = create_body("Earth",   5.927e24)
mars    = create_body("Mars",    6.417e23)
jupiter = create_body("Jupiter", 1.898e27)
saturn  = create_body("Saturn",  5.683e26)
uranus  = create_body("Uranus",  8.681e25)
neptune = create_body("Neptune", 1.024e26)

# Optional: export planets as a list for easy access
all_planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
