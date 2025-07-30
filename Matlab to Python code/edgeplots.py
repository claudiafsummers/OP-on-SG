import numpy as np
import matplotlib.pyplot as plt

from SGorthoPolyEdge23pk import SGorthoPolyEdge23pk
from SGorthoPolyEdge23sk import SGorthoPolyEdge23sk
from SGorthoPolyEdge13pk import SGorthoPolyEdge13pk
from SGorthoPolyEdge23phik import SGorthoPolyEdge23phik
from SGorthoPolyEdge13phik import SGorthoPolyEdge13phik

def edgeplots(T, num, flag):
    '''
    plots the polynomials along the edges, plots them all together

    INPUT:
    T - large matrix with the values of the monomials up to level m=7
    num - the number of polynomials to plot
    flag = 1 plots the edge of the antisymm OP along the bottom edge
    flag = 2 plots the edge of the symm OP along the bottom edge
    flag = 3 plots the edge of the antisymm OP along the side edge
    '''
    
    for j in range(num):
        if flag == 1:
            edge = SGorthoPolyEdge23pk(T, j)
            titlestring = 'bottomedge'
            xlabelstr = 'bottom edge'
            legstring = 'Q_{'
            filestring = 'p'
        elif flag == 2:
            edge = SGorthoPolyEdge23sk(T, j)
            titlestring = 'bottomedge'
            xlabelstr = 'bottom edge'
            legstring = 'S_{'
            filestring = 's'
        elif flag == 3:
            edge = SGorthoPolyEdge13pk(T, j)
            titlestring = 'sideedge'
            xlabelstr = 'side edge'
            legstring = 'Q_{'
            filestring = 'p'
        elif flag == 4:
            edge = SGorthoPolyEdge23phik(T, j)
            titlestring = 'bottomedge'
            xlabelstr = 'bottom edge'
            legstring = r'$\phi_{'
            filestring = 'phi'
        else:
            edge = SGorthoPolyEdge13phik(T, j)
            titlestring = 'sideedge'
            xlabelstr = 'side edge'
            legstring = r'$\phi_{'
            filestring = 'phi'

        # Reset plot
        plt.clf()

        z = np.zeros_like(edge)

        plt.plot(np.real(edge), linewidth=4)
        plt.plot(z, linewidth=2, color='black')

        # Formatting
        plt.xlim(0, len(edge))
        plt.xticks([])
        plt.xlabel(xlabelstr, fontsize=30)
        plt.ylim(-4, 4)
        plt.title(f"{legstring}{j}" + "}", fontsize=40)
        plt.tick_params(labelsize=30)

        # Save as PNG
        filename = f"{filestring}{j}{titlestring}"
        plt.savefig(f"{filename}.png", format='png')
        
    return
