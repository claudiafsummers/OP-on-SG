import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from SG import SG

def gaskplot(f, m):
    """
    Plots a function defined on the level m vertices of the Sierpinski Gasket.
    From http://www.math.cornell.edu/~mhall/SGprograms/gaskplot.m

    INPUT:
    f - Function values at the vertices of SG with size 3**(m+1)
    m - Level of SG

    OUTPUT: Plots a figure of SG
    """
    y = SG(m)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    f = np.asarray(f).flatten()  # Flatten in case f is a column vector

    for k in range(3**m):
        idx = slice(3 * k, 3 * k + 3)  # Selects 3 points per triangle edge
        x_coords = np.append(y[idx, 0], y[3 * k, 0])  # Close the loop
        y_coords = np.append(y[idx, 1], y[3 * k, 1])
        z_coords = np.append(f[idx], f[3 * k])

        ax.plot3D(x_coords, y_coords, z_coords)

    return
