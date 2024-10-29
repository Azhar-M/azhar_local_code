import numpy as np
import matplotlib.pyplot as plt

# Create a 3D array of x, y coordinates
x = np.linspace(-20, 20, 41)
y = np.linspace(-20, 20, 41)

# Create a meshgrid
x_1, y_1 = np.meshgrid(x, y)

# Compute the ellipse values using the meshgrid arrays
ellipse = x_1**2 * 2 + 4 * y_1**2

# Plot the contour
plt.contourf(x_1, y_1, ellipse, cmap='jet')
plt.colorbar()
plt.show()

