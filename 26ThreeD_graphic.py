# 3d_graphic.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_plot():
    """
    Generates a 3D sine wave plot.
    """
    # Create a figure and a 3D Axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the data for the 3D plot
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    # Plot the surface
    ax.plot_surface(x, y, z, cmap='viridis')

    # Add labels
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('3D Sine Wave')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    generate_3d_plot()
