# Mandelbrot_Set.py

import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Generate the Mandelbrot set image
def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    n3 = np.empty((width, height))
    
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    
    return (r1, r2, n3)

# Set the parameters for the Mandelbrot set
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 256

# Generate the Mandelbrot set
r1, r2, n3 = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# Plot the Mandelbrot set
plt.figure(dpi=100)
plt.imshow(n3.T, extent=[x_min, x_max, y_min, y_max], cmap='hot')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
