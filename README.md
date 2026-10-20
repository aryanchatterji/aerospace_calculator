# Historical Aerospace Calculator: ISRO Launch Vehicle Database

## Abstract
This repository contains a standalone, Python-based orbital mechanics calculator designed to evaluate mission feasibility. By leveraging historical launch data from the Indian Space Research Organisation (ISRO) spanning multiple decades, the tool utilizes the Tsiolkovsky rocket equation to calculate required delta-v ($\Delta v$) metrics and analyze the statistical probability of mission success for various vehicle configurations (including SLV, ASLV, PSLV, and GSLV).

## Execution Instructions (How to Run)

To execute the orbital mechanics simulator and calculate fuel mass requirements, run the following command in your terminal:

`python aerospace_calculator.py`

**Execution Requirements & Expected Behavior:**
1. **Dataset Dependency:** The script requires the `isro_database.csv` file to be present in the root directory to dynamically parse the 215-mission dataset.
2. **Interactive CLI:** Upon execution, the terminal will prompt you to input a target launch vehicle family (SLV to LVM3) and dynamically list available historical configurations.
3. **Physics Output:** After inputting a target Delta-V (m/s), the engine will run the Tsiolkovsky Rocket Equation and output a mission report detailing whether the vehicle's physical fuel tanks can support the maneuver.

## Core Architecture

### 1. The Physics Engine
*   **Module:** `aerospace_calculator.py`
*   **Physics Implemented:** Functions as the core computational engine, applying the Tsiolkovsky rocket equation to user-defined mission parameters. It calculates ideal velocity changes based on theoretical specific impulse ($I_{sp}$) and mass fractions.

### 2. The Historical Database
*   **Data Source:** `isro_database.csv`
*   **Implementation:** A curated dataset of historical ISRO missions. The calculator cross-references calculated mission requirements against this historical database to extrapolate success probabilities based on past vehicle performance under similar aerodynamic and orbital loads.

## Computational Methodologies Demonstrated
*   **Orbital Mechanics:** Practical application of fundamental rocketry kinematics in a programmatic environment.
*   **Data Parsing & Statistical Analysis:** Reading, filtering, and cross-referencing external CSV datasets to drive logic-based outputs.
*   **Educational Outreach:** This codebase serves as the computational foundation for a five-part educational video series breaking down rocket kinematics and ISRO's developmental timeline.

## Technical Stack
*   **Language:** Python 3.x
*   **Data Handling:** Standard Python I/O methodologies for parsing unstructured and structured data files (`.csv`, `.txt`, `.pdf`).

---
*Note: This repository is maintained as a public portfolio of computational physics research and aerospace engineering development.*
