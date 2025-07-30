import numpy as np
import matplotlib.pyplot as plt

from SGorthoPolyssk import SGorthoPolyssk
from gaskplot import gaskplot

def orthoplotssk(T,Num):
    '''
    plots the antisymmetric orthogonal polynomials 

    INPUT:
    - T: array with values of monomial to required level
    - num: number of monomials to be plotted (max degree is num-1)
    '''

    for j in range(Num):
        plt.figure() 
        p = SGorthoPolyssk(T, j)
        gaskplot(p, 7)

        ax = plt.gca()
        ax.set_zlim(-10, 10)
        plt.title(rf'$S_{{{j}}}$', fontsize=40)
        ax.tick_params(labelsize=20)

        plt.savefig(f"s{j}", dpi=300) 
        plt.show() 
        plt.close()
    
    return 
