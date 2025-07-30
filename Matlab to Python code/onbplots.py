import numpy as np
import matplotlib.pyplot as plt

from SGorthoPolyspk import SGorthoPolyspk
from SGorthoPolyssk import SGorthoPolyssk
from gaskplot import gaskplot

def onbplots(T,Num):
    '''
    plots the ONB polynomials  (each OP is orthogonal to its rotations)

    INPUT:
    - T: array with values of monomial to required level
    - num: number of monomials to be plotted (max degree is num-1)
    '''

    for j in range(Num):
        plt.cla()
        Q=SGorthoPolyspk(T,j)
        S=SGorthoPolyssk(T,j)
        gaskplot(np.sqrt(2/3)*Q + np.sqrt(1/3)*S,7)    
 
    ax = plt.gca()
    ax.set_zlim(-10, 10)
    plt.title(rf'$\phi_{{{j}}}$', fontsize=40)
    ax.tick_params(labelsize=20)
    filename = f"phi{j}"
    plt.savefig(f"{filename}.png", format='png')    # Save each plot as an png file

    return 
