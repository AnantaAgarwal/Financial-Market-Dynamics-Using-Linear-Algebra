# Financial-Market-Dynamics-Using-Linear-Algebra
This project analyzes how market stress spreads across interconnected banks using Linear Algebra and Python. It models bank connections, studies system stability, identifies risky and stable market situations, and visualizes how stress propagates over time through simulations.
# How Market Shocks Travel Through the Banking System

## Overview
This project studies how market stress spreads across interconnected banks using Linear Algebra and Python. Instead of analyzing banks individually, the banking system is modeled as a network where connections between banks influence how stress propagates during economic turbulence.

The project focuses on understanding system behavior, risk patterns, and stability in a clear and visual way. It is designed to be understandable even for readers without a strong mathematics or finance background.

---

## Objectives
- Represent bank interconnections using a matrix-based model  
- Study system stability using matrix properties  
- Identify high-risk and low-risk market situations  
- Analyze how market stress spreads over time  
- Explain financial system behavior using simple visuals  

---

## Problem Statement
Banks are connected through lending, investments, and market activities. Because of these connections, financial stress does not remain limited to one bank and can spread across the entire system.

This project aims to understand:
- How stress propagates across connected banks  
- Which banks experience stronger pressure  
- Which market situations are more dangerous for the system  

---

## Methodology

### 1. System Modeling
- Each bank is represented as a node  
- Connections between banks are modeled using a square matrix  
- External market stress is represented using a vector  

### 2. Matrix Analysis
The following properties are analyzed to understand system behavior:
- Symmetry (mutual influence between banks)
- Rank (independent contribution of banks)
- Determinant (system solvability and stability)
- Trace (overall internal strength)
- Null space (whether any shock is ignored)

### 3. System Response
The system of equations `A × x = b` is solved to observe how banks respond to an external market shock.

### 4. Eigenvalue Analysis
- Eigenvalues are used to identify stressful and stable market situations  
- Eigenvectors represent patterns in which banks move together  

### 5. Validation
The Cayley–Hamilton theorem is verified to ensure mathematical correctness of the model.

### 6. Portfolio Risk Assessment
A simple investment portfolio is analyzed to check whether it aligns with high-risk system-wide patterns.

### 7. Simulation
A time-based simulation is performed to visualize how stress spreads across banks over time.

---

### Bank Connection Matrix
```python
import numpy as np

A = np.array([
    [2, -1,  0,  0],
    [-1, 2, -1,  0],
    [0, -1,  2, -1],
    [0,  0, -1,  2]
])
