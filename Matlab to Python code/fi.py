def fi(x,qi):
    '''
    This function is a contractive similarity of the plane centered at the point qi of dilation factor 1/2.

    INPUT:
    x - point in the plane
    qi - point toward which to contract distance by 1/2

    OUTPUT: evaluates the similarity

    from http://www.math.cornell.edu/~mhall/SGprograms/fi.m
    '''

    return qi + 0.5*(x-qi)
