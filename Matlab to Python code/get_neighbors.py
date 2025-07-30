import numpy as np

from alternate_address import alternate_address

def get_neighbors(v,m):
    ''' This function finds the addresses of those edges which are adjacent to a given vertex. 
    If the given vertex is on the boundary of SG we return two copies of each of the adjacent edges. 

    INPUT:
    v - address of the vertex (vector with length = m+1)
    m - level of SG (meaning we have 3^(m+1) points)

    OUTPUT:
    nbhd - matrix with 4 rows, with each row giving the address of an edge touching given vertex

    e.g.
         /\
        /__\
       /\  /\
      /__\/__\

    gneighbors([1 2], 1) = [1 1; 1 3; 2 3; 2 2]
    '''

    w = alternate_address(v,m)  # find alternate address of our vertex

    one = np.ones_like(v)
    di = np.zeros_like(v)
    di[len(di)] = 1

    ''' Given the address of a point corresponding to that point's position within a given cell, 
    the incident edges in that cell have the two other vertex addresses corresponding to that cell '''

    nbhd = np.zeros((4, len(v)), dtype=int)
    nbhd[0,:] = (np.mod(v - one + 2 * di, 3)) + one 
    nbhd[1,:] = (np.mod(v - one + 1 * di, 3)) + one 
    nbhd[2,:] = (np.mod(w - one + 2 * di, 3)) + one 
    nbhd[3,:] = (np.mod(w - one + 1 * di, 3)) + one 

    return nbhd
