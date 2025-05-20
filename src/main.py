import numpy as np
import matplotlib.pyplot as plt
from body import Body


def main():
    earth = Body("Earth", 6, np.array([1,2,3]), [0,0,0])
    sun = Body("Sun", 100000, np.array([1,2,13]), [0,0,0])
    print(earth.force_from(sun))
    print(earth)


    return 0

if __name__ == "__main__":
    main()