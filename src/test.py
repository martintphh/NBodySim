from astroquery.jplhorizons import Horizons

# Julianisches Datum für 2025-01-01 00:00 UTC
epoch = 2460676.5

obj = Horizons(id='Earth', location='500@0', epochs=epoch)
vecs = obj.vectors()

print("Position [AU]:", vecs[0]['x'], vecs[0]['y'], vecs[0]['z'])
print("Velocity [km/s]:", vecs[0]['vx'], vecs[0]['vy'], vecs[0]['vz'])
