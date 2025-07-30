import numpy as np

def address(k,m):
    '''
    This function returns a vector listing the address of a given index k in a level m SG-type ordering (TLR ordering).

    INPUT: 
    k - the index whose address to find
    m - level of SG (meaning we have 3^(m+1) points) 

    OUTPUT: 
    v - vector of length m+1, listing off a sequence of 0's, 1's,and 2's, which locate the given index.

    e.g.
    k = 4, m = 1 returns [2 1] (second cell of m=1, first position)
    k = 21 m = 2 returns [3 1 3] (third cell of m=1, first cell of m=2, third position)
    '''
    v = []
    
    while m > 0:
        r = (k - 1) // (3 ** m)
        v.append(r + 1)
        k = k - r * (3 ** m)
        m -= 1

    v.append(k)  # Final address component
    v = np.array(v)
    return v
