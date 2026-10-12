# Historical Aerospace Calculator: ISRO Launch Vehicle Database

## Abstract
This repository contains a standalone, Python-based orbital mechanics calculator designed to evaluate mission feasibility. By leveraging historical launch data from the Indian Space Research Organisation (ISRO) spanning multiple decades, the tool utilizes the Tsiolkovsky rocket equation to calculate required delta-v ($\Delta v$) metrics and analyze the statistical probability of mission success for various vehicle configurations (including SLV, ASLV, PSLV, and GSLV).

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
