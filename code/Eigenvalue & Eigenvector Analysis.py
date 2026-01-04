#eigenvalues and eigenvectors
eigenvalues , eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A : \n",eigenvalues,"\n")
print("Eigenvectors of A : \n",eigenvectors,"\n")

#Ploting Eigenvectors 
import numpy as np
import matplotlib.pyplot as plt

# Bank names
banks = ['SBI', 'ICICI', 'HDFC', 'Axis']

# Take one eigenvector (example: dominant eigenvector)
eigenvector = [-0.3717, 0.6015, -0.6015, 0.3717]

plt.figure()
plt.bar(banks, eigenvector)
plt.axhline(0)
plt.xlabel("Banks")
plt.ylabel("Response Direction")
plt.title("Bank Reaction Pattern under a Market Situation")
plt.show()

plt.figure()

#Plotting Eigenvectors as line
for i, value in enumerate(eigenvector):
    plt.arrow(i, 0, 0, value, head_width=0.05, length_includes_head=True,color="red")

plt.xticks(range(len(banks)), banks)
plt.axhline(0)
plt.ylabel("Direction of Response")
plt.title("Bank Reaction Pattern under a Market Situation")
plt.show()

# Cayley - Hamilton Theorem verification

#identity matrix
I = np.eye(4)

#Eigenvalue matrix
eigenvalues_A = np.array([3.61803399 ,2.61803399, 0.38196601 ,1.38196601])

#characteristics polynomial coefficients
coeffs = np.poly(eigenvalues_A)
print(coeffs,"\n")

#result
result = (coeffs[0]*A@A@A@A +
          coeffs[1]*A@A@A +
          coeffs[2]*A@A +
          coeffs[3]*A +
          coeffs[4]*I)

print(result)
