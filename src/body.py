# src.body
import numpy as np

class Body:
    def __init__(self, name, mass, position, velocity):
        self.name = name #str
        self.mass = mass #float
        self.position = np.array(position, dtype=float) #ndarray 3D
        self.velocity = np.array(velocity, dtype=float) #ndarray 3D
        self.force = np.zeros(3) #can be updated later

    def __repr__(self):
        return f"Body {self.name}: position={self.position}, velocity={self.velocity}"

    def force_from(self, other_body, G = 6.6743e-11):
        """force from other_body on self
        units AU, where G=4pi^2"""

        r_vec = other_body.position - self.position
        r_magnitude = np.linalg.norm(r_vec)
        if r_magnitude == 0:
            return np.zeros(0)
        force_magnitude = G * self.mass * other_body.mass / r_magnitude**2
        force_vec = force_magnitude * r_vec / r_magnitude

        return force_vec
