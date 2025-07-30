import numpy as np

from getorder import getorder
from alternate_index import alternate_index

def T(m):
    ''' This function reads the monomials in polydata_20.txt '''

    m = 7
    T = np.zeros((3**(m + 1), 20, 3)) # T: values, degree, type
    indices = getorder()

    with open('polydata_20.txt', 'r', encoding='utf-8-sig') as fid:
        for j in range(20):       # 0-based
            for i in range(3):
                for k in range(3282):
                    index = indices[k]
                    tline = fid.readline()
                    T[index-1, j, i] = float(tline.strip())

    for j in range(20):
        for i in range(3):
            for k in range(3**(m + 1)):
                if T[k, j, i] == 0:
                    v = alternate_index(k, m)
                    T[k, j, i] = T[v, j, i]

    T[0, 0, 0] = 1
    T[3**8 - 1, 0, 0] = 1

    return T
