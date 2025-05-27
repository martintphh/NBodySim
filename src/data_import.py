from astroquery.jplhorizons import Horizons
import json
import numpy as np


def main():
    planets = {"Sun":10, "Mercury":199, "Venus":299, "Earth":399, "Mars":499, "Jupiter":599, "Saturn":699, "Uranus":799, "Neptune":899}
    epoch = 2460676.5 #JD für 01.01.2025

    data = {}

    for planet, planet_id in planets.items():
        obj = Horizons(
            id=planet_id,
            id_type='id',
            location="500@0",  #heliozentrisch
            epochs = epoch
        )
        vecs = obj.vectors()
        
        planet_data = {}
        
        """for i in ('x', 'y', 'z', 'vx', 'vy', 'vz'):
            planet_data[f"{i}"] = float(vecs[0][i])"""

        position = []
        for i in ("x", "y", "z"):
            position.append(float(vecs[0][i]))
        planet_data["position"] = position

        velocity = []
        for i in ("vx", "vy", "vz"):
            velocity.append(float(vecs[0][i]))
        planet_data["velocity"] = velocity
        data[planet] = planet_data

    with open("planet_data.json", "w") as f:
        json.dump(data, f, indent=2)
    
    print("data saved successfully!")
  
if __name__ == "__main__":
    main()

