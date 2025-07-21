# N-Body Simulation

A classical N-body simulation of our solar system using Newtonian gravity.  
The project implements both the Euler method and the fourth-order Runge-Kutta method for numerical integration.  
It visualizes planetary orbits and analyzes total, potential, and kinetic energy over time.

## Features

- Simulation of gravitational forces between selected solar system planets
- 2D visualization of planetary trajectories (static plots and animations)
- Monitoring of total, kinetic, and potential energy
- Configurable time step, duration, and integration method

## Installation

```bash
git clone https://github.com/username/n-body-simulation.git
cd n-body-simulation
pip install -r requirements.txt
```

## Usage

All simulation parameters are configured in [`src/config/config.py`](src/config/config.py), including:

- `bodies`: List of celestial bodies to include (e.g., `sun`, `earth`, `mars`)
- `dt`: Time step (e.g., `1` seconds)
- `steps`: Number of simulation steps / duration of simulation (e.g., `60` steps with `dt = 1` is one hour)
- `integrator`: Numerical method (`"euler"`, `"rk4"`, etc.)
- `pathname`: Optional suffix for result files (e.g., `"5bodies_5y_rk4"`)

To run the simulation and generate plots and animations:

```bash
python3 src/main.py
```

## Project Structure

```bash
.
├── LICENCE
├── README.md
├── requirements.txt
├── results
│   ├── animation_5bodies_5y_rk4.mp4
│   └── plot_5bodies_5y_rk4.png
└── src
    ├── __init__.py
    ├── __pycache__
    ├── config
    ├── core
    ├── main.py
    └── visualization
```

## Backround

The N-body problem ist a central problem in classical mechanics. It describes the evolution of multiple (N) bodies unter mutual gravitational attraction, following Newton's law of gravitation. Analytical solutions only exist for a two-body case (N = 2), hence for N > 2 numerical methods must be considered. This project illustrates numerical techniques for solving such systems and their limitations over long timescales.


## Future Work
- Add plots/animations of energy (total, potential, kinetic) over time to compare euler and rk4
- Add function to analyse perihel rotation

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Initial conditions based on NASA JPL HORIZONS
- Developed as part of a physics project for individuall learning purposes

## Contact

Martin Tinhof – [martin.tinhof01@gmail.com]  
Project link: [https://github.com/martintinhof/NBodySim](https://github.com/martintinhof/NBodySim)


