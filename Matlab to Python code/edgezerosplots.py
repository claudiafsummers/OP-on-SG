import numpy as np
import matplotlib.pyplot as plt

from edgezeros4 import edgezeros4

def edgezerosplots(T,Num,flag):
    '''
    Plots the zeros along the edges of the OP_j for j=0,...,Num-1

    INPUT:
    T - large matrix with the values of the monomials up to level m=7
    Num - Number of edges to plots (OP_j for j=0, ..., Num-1)
    if flag = 1, then using antisymm OP
    if flag = 2, then using symm OP
    '''

    for j in range(Num):
        edgezeros4(T,j,flag)
        if flag == 1:
            filestring='p'
        else:
            filestring='s'

        # Save current figure
        filename = f"{filestring}{j}edgezeros"
        plt.savefig(f"{filename}", dpi=300)
        plt.show()
        
    return
