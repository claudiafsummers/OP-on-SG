import numpy as np
import matplotlib.pyplot as plt

from gaskplot import gaskplot

def monomialplots(T, num):
    '''
    INPUT:
    - T: array with values of monomial to required level
    - num: number of monomials to be plotted (max degree is num-1)
    '''

    for j in range(num):
        plt.clf()
        gaskplot(T[:, j, 0], 7)
        plt.title(f"$P_{{{j}1}}$", fontsize=40)
        plt.gca().tick_params(labelsize=20) 
        plt.savefig(f"monomial{j}1.png", format='png') # Save the figure as a PNG file

        plt.clf()
        gaskplot(T[:, j, 1], 7)
        plt.title(f"$P_{{{j}2}}$", fontsize=40)
        plt.gca().tick_params(labelsize=20) 
        plt.savefig(f"monomial{j}2.png", format='png') # Save the figure as a PNG file

        plt.clf()
        gaskplot(T[:, j, 2], 7)
        plt.title(f"$P_{{{j}3}}$", fontsize=40)
        plt.gca().tick_params(labelsize=20) 
        plt.savefig(f"monomial{j}3.png", format='png') # Save the figure as a PNG file

    return
