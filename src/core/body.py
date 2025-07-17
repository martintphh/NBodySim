
import numpy as np

#Gravitational constant in SI units [m^3 kg^-1 s^-2]
G_SI = 6.6743e-11

#Astromical unit in meters
AU_in_m = 1.495978707e11

#Gravitational constant convertet for AU units
G_AU = G_SI / AU_in_m**3

class Body:
    """
    Represents a celestial body (sun, planet, etc.)

    Attributes:
        name (str): Name of the body
        mass (float) Mass of the body 
        position (ndarray) 3D position vector (in AU)
        velocity (ndarray) 3D velocity vector (in AU/day) 
    """
    def __init__(self, name, mass, position, velocity):
        self.name = name #str
        self.mass = mass #float
        self.position = np.array(position, dtype=float) #ndarray 3D
        self.velocity = np.array(velocity, dtype=float) #ndarray 3D
        self.force = np.zeros(3) #can be updated later

    def __repr__(self):
        """
        Return a readable string represantation of the body for debugging
        """
        return f"Body {self.name}: position={self.position}, velocity={self.velocity}"

    def force_from(self, other_body, G = G_AU):
        """
        Calculate gravitational force exerted on self from another body.

        Parameter:
            other_body (Body): Celestial body applying the force
            G (float): Gravitational constant

        Returns:
            np.array: Force vector acting on self due to the gravitational influence of other_body
        """

        r_vec = other_body.position - self.position     #Vector from self to other_body
        r_magnitude = np.linalg.norm(r_vec)             #Euclidian distance between self and other_body
        
        if r_magnitude == 0:
            #avoiding devision by 0 if bodies would overlap
            return np.zeros(0)
        
        force_magnitude = G * self.mass * other_body.mass / r_magnitude**2          #Force magnitude
        force_vec = force_magnitude * r_vec / r_magnitude                           #Force direction vector

        return force_vec
