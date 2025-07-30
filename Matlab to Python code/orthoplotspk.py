import numpy as np
import matplotlib.pyplot as plt

from SGorthoPolyspk import SGorthoPolyspk
from gaskplot import gaskplot

def orthoplotspk(T,Num):
    '''
    plots the antisymmetric orthogonal polynomials 

    INPUT:
    - T: array with values of monomial to required level
    - num: number of monomials to be plotted (max degree is num-1)
    '''

    for j in range(Num):
        plt.clf()  
        plt.close()  
        plt.figure()
        p = SGorthoPolyspk(T,j)
        gaskplot(p,7)

        ax = plt.gca()
        ax.set_zlim(-10, 10)
        plt.title(rf'$Q_{{{j}}}$', fontsize=40)
        ax.tick_params(labelsize=20)
        plt.savefig(f"p{j}", dpi=300)
        plt.show()
    
    return 
