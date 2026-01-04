import numpy as np

# Portfolio vector
portfolio = np.array([1, 1, 0, 0])

# Take dominant eigenvectors (columns)
dominant_vectors = np.array([
    [-0.3717, -0.6015],
    [ 0.6015,  0.3717],
    [-0.6015,  0.3717],
    [ 0.3717, -0.6015]
])

# Solve least squares
coeffs, residuals, rank, s = np.linalg.lstsq(dominant_vectors, portfolio, rcond=None)

print("Residual error:", residuals)

import numpy as np
import matplotlib.pyplot as plt

# Matrix A
A = np.array([
    [2, -1,  0,  0],
    [-1, 2, -1,  0],
    [0, -1,  2, -1],
    [0,  0, -1,  2]
])

# Initial shock / starting condition
x = np.array([1, 1, 0, 0])   # SBI & ICICI affected first

# Store results
steps = 6
history = [x]

for i in range(steps):
    x = A @ x
    history.append(x)

history = np.array(history)

# Plot
plt.figure()
plt.plot(history)
plt.xlabel("Time steps")
plt.ylabel("System response")
plt.title("How Bank Values Change Over Time Under Market Stress")
plt.legend(['SBI', 'ICICI', 'HDFC', 'Axis'])
plt.show()
