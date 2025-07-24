1. UI (Frontend)
   - [ ] Redesign layout (cleaner and modern)
   - [ ] Add tabs or sections (e.g., Geometry | Simulation | Results)
   - [ ] Add theme support (light/dark mode)
   - [ ] Add settings dialog (resolution, background color, units)
   - [ ] Input validation (only allow valid NACA codes)

	  ![alt text](image.png)

2. Geometry Generation
   - [x] Generate airfoil from NACA 4-digit code
   - [ ] Add support for 5-digit and 6-series codes
   - [ ] Export to CSV or TXT (coordinates)
   - [ ] Display camber line

3. Angle of Attack Transformation
   - [x] Apply rotation to geometry
   - [ ] Add real-time slider for AoA
   - [ ] Limit AoA input (e.g., -15° to +15°)

4. Aerodynamic Solver (Mini CFD)
   - [ ] Basic inviscid flow simulation
   - [ ] Add pressure distribution visualization
   - [ ] Calculate lift coefficient
   - [ ] Add simple panel method or vortex lattice model

5. Post-Processing
   - [ ] Export plots as images
   - [ ] Add color mapping (pressure, velocity)
   - [ ] Show result table: Cl, AoA, NACA, etc.

6. Data/Settings Management
   - [ ] Save/load previous sessions
   - [ ] Save default settings (JSON or XML)
   - [ ] Implement configuration file

7. Testing & Debugging
   - [ ] Unit tests for geometry generation
   - [ ] Check UI responsiveness
   - [ ] Validate solver outputs with known data

-------------------------------
FUTURE IDEAS
-------------------------------
- [ ] Airfoil comparison tool (side-by-side view)
- [ ] 3D visualization (extruded wing)
- [ ] Export to STL for printing
- [ ] Add turbulence models (basic RANS)
- [ ] Educational mode (explain steps with tooltips)


