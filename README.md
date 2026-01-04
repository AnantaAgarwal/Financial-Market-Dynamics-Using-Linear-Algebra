# How Market Shocks Travel Through the Banking System

## Overview
This project examines how **market stress propagates through an interconnected banking system** using concepts from **Linear Algebra** and **system-level modeling**.  
Instead of analyzing banks in isolation, the banking sector is represented as a **network**, where financial interconnections influence how shocks spread during periods of economic instability.

The focus is on understanding **system behavior, risk patterns, and stability** in a simplified and intuitive manner.

---

## Motivation
Modern financial systems are highly interconnected.  
A shock affecting one institution can quickly spread to others, amplifying systemic risk.

This project aims to demonstrate how mathematical modeling helps:
- Capture financial contagion effects
- Identify vulnerable institutions
- Understand stability at a system-wide level

---

## Objectives
- Model inter-bank relationships using matrix-based representations  
- Analyze stability using fundamental matrix properties  
- Study how external market stress impacts connected banks  
- Identify risky and stable market conditions  
- Communicate insights in a clear, non-technical way  

---

## Problem Statement
Banks are linked through lending, borrowing, and other financial exposures.  
Due to these interdependencies, stress originating in one bank can propagate through the entire system.

This project seeks to understand:
- How stress spreads across the banking network  
- Which banks are more affected by market shocks  
- Why system-level analysis is essential for risk assessment  

---

## Methodology

### 1. System Modeling
- Banks are represented as nodes in a financial network  
- Inter-bank connections are modeled using a square matrix  
- External market stress is represented as an input vector  

---

### 2. Matrix-Based Analysis
Key matrix properties are examined to assess system behavior:
- Symmetry  
- Rank  
- Determinant  
- Trace  
- Null Space  

These properties help evaluate **connectivity, solvability, and stability**.

---

### 3. System Response
The system behavior is analyzed by studying how banks collectively respond to an external market shock.  
This helps identify which institutions experience stronger pressure due to network effects.

---

### 4. Eigenvalue Analysis
- Eigenvalues indicate whether the system behaves in a stable or stressful manner  
- Eigenvectors reveal collective movement patterns among banks  

This analysis highlights conditions under which market stress may amplify or dissipate.

---

### 5. Stress Propagation Simulation
A time-based simulation is used to visualize how stress evolves across the banking network, offering insights into dynamic behavior during prolonged market disturbances.

---

## Tools and Technologies
- Python  
- Linear Algebra  
- NumPy  
- Matplotlib  
- SymPy  

---

## Key Insights
- Banks do not respond equally to market stress  
- Highly connected banks experience greater systemic pressure  
- Certain market conditions are inherently more unstable  
- System-level analysis provides deeper risk understanding than isolated evaluation  

---

## Conclusion
This project demonstrates how **linear algebra and network modeling** can be applied to analyze **financial system stability**.  
By focusing on interconnections rather than individual institutions, it provides a clearer understanding of **risk propagation and systemic vulnerability**.

---

## Future Scope
- Expansion to larger and more complex banking networks  
- Incorporation of probabilistic market shocks  
- Use of real-world financial exposure data  
- Extension toward stress-testing and risk forecasting models  







