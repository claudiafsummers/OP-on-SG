from index import index
from address import address
from alternate_address import alternate_address

def alternate_index(k,m):
    ''' 
    This function finds the alternative index for a given point in TLR ordering on SG. If the point is on the boundary of SG, 
    (and hence has only one such index) the same address vector is returned.

    INPUT: 
    k - index of the point
    m - level of SG (meaning we have 3^(m+1) indices) 

    OUTPUT: alternate index for the same point

    e.g. 
    alternate_index(2,1) returns 4
    alternate_index(3,1) returns 7
    '''

    # We convert to an address, go through the alternate address function, and convert back to an index

    v = address(k,m)
    w = alternate_address(v,m)
    return index(w,m)
