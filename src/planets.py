from body import Body
import numpy as np
import json

AU = 1.497e11   #AU in m Umrechungsfaktor
AU_per_d = 24 * 3600 # AU/d in AU/s

with open("planet_data.json", "r") as file:
    data = json.load(file)

print(data.keys())
print(data["Earth"]["position"])


"""
earth = Body(
        name="Earth",
        mass =5.972e24,
        position=np.array([1.496e11,0.,0.]),
        velocity=np.array([0.,29780.,0.]))

sun = Body("Sun", 
    mass=1.9885e30,
    position=np.array([0,0,0]),
    velocity=np.array([0.,0.,0.]))
    
jupiter = Body("Jupiter",
    mass=1.898e27,
    position=np.array([7.758e11,0,0])/AU,
    velocity=np.array([0,13058,0])/AU)

venus = Body("Venus",
    mass=4.867e24,
    position=np.array([1.082e11,0,0])/AU,
    velocity=np.array([0,35033,0])/AU)




e = Body(
        name="Earth",
        mass =5.972e24,
        position=np.array([1.496e11,0.,0.]),
        velocity=np.array([0.,29780.,0.]))

s = Body("Sun", 
    mass=1.9885e30,
    position=np.array([0,0,0]),
    velocity=np.array([0.,0.,0.]))
    
v = Body("Venus",
    mass=4.867e24,
    position=np.array([0,1.082e11,0]),
    velocity=np.array([35033,0,0]))


mercury = Body(
    name="Mercury",
    mass=3.285e23,
    position=np.array(data["Mercury"]["position"]),
    velocity=np.array(data["Mercury"]["position"])*AU_per_d
)
"""

earth = Body(
    name="Earth",
    mass=5.927e24,
    position=np.array(data["Earth"]["position"]),
    velocity=np.array(data["Earth"]["velocity"])/AU_per_d
)

sun = Body(
    name="Sun", 
    mass=1.9885e30,
    position=np.array(data["Sun"]["position"]),
    velocity=np.array(data["Sun"]["velocity"])/AU_per_d
)
    
jupiter = Body(
    name="Jupiter",
    mass=1.898e27,
    position=np.array(data["Jupiter"]["position"]),
    velocity=np.array(data["Jupiter"]["velocity"])/AU_per_d
)

venus = Body(
    name="Venus",
    mass=4.867e24,
    position=np.array(data["Venus"]["position"]),
    velocity=np.array(data["Venus"]["velocity"])/AU_per_d
)

mercury = Body(
    name="Mercury",
    mass=3.285e23,
    position=np.array(data["Mercury"]["position"]),
    velocity=np.array(data["Mercury"]["velocity"])/AU_per_d
)

mars = Body(
    name="Mars",
    mass=6.417e23,
    position=np.array(data["Mars"]["position"]),
    velocity=np.array(data["Mars"]["velocity"])/AU_per_d
)

saturn = Body(
    name="Saturn",
    mass=5.683e26,
    position=np.array(data["Saturn"]["position"]),
    velocity=np.array(data["Saturn"]["velocity"])/AU_per_d
)

uranus = Body(
    name="Uranus",
    mass=8.681e25,
    position=np.array(data["Uranus"]["position"]),
    velocity=np.array(data["Uranus"]["velocity"])/AU_per_d
)
neptune = Body(
    name="Neptune",
    mass=1.024e26,
    position=np.array(data["Neptune"]["position"]),
    velocity=np.array(data["Neptune"]["velocity"])/AU_per_d
)

"""
bodies = [earth, sun, mercury, venus, mars, jupiter, saturn, uranus, neptune]
for body in bodies:
    print(body.name)
    print(body.position.shape)
    print(body.velocity.shape)"""