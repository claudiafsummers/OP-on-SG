import numpy as np
from matplotlib import pyplot as plt

from monomials import generate_T, generate_T_symmetric
from plotting import eval_op
from util import address_from_index

def monomial_left_edge(deg, k, level=7, T=None, symm=False):
    '''
        Args: 
        deg - Maximum degree monomial required
        k - Type of Monomial (k = 1, 2, 3)
        level - The level we would like to plot each monomial
        T - array of monomial values at the required level and degree or 
            tuple of (filename of .npz/.npy file containing this array , array name key string)
        symm - Boolean representing whether or not the fully symmetric orthogonal polynomials are needed

        Returns: 
        Plot of the left edge of symmetric and anti symmetric monomials

    '''
    k = k - 1

    if T is None:
        print('Generating array of monomial values. This may take some time...')
        if symm:
            T = generate_T_symmetric(level, deg, frac=False)
        else:
            T = generate_T(level, deg, frac=False)
    elif isinstance(T, (tuple)):
        print('Using preloaded monomial values.')
        filename, arr = T
        T = np.load(filename, allow_pickle=False)[arr]  

    edge_indices = []
    for i in range(3**(level + 1)):
        addr = address_from_index(level, i + 1)
        addr = ''.join(str(int(x)) for x in reversed(addr))
        digits = set(addr)
        if digits <= {'0', '1'}:
            edge_indices.append(i)
    
    edge_array = T[k, edge_indices, :]

    num_points, max_deg_plus_1 = edge_array.shape
    x_vals = range(num_points)

    for deg in range(max_deg_plus_1):
        plt.figure()  # <-- new pop-up window
        plt.plot(x_vals, edge_array[:, deg], marker='o', markersize=2)
        plt.title(f"Left — Monomial Degree {deg}")
        plt.xlabel("Index along edge")
        plt.ylabel(f"P_{deg}(x)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()



def monomial_bottom_edge(deg, k, level=7, T=None, symm=False):
    '''
    Args: 
    deg - Maximum degree monomial required
    k - Type of Monomial (k = 1, 2, 3)
    level - The level we would like to plot each monomial
    T - array of monomial values at the required level and degree or 
        tuple of (filename of .npz/.npy file containing this array , array name key string)
    symm - Boolean representing whether or not the fully symmetric orthogonal polynomials are needed

    Returns: 
    Plot of the bottom edge of symmetric and anti symmetric monomials

    '''
    k = k - 1

    if T is None:
        print('Generating array of monomial values. This may take some time...')
        if symm:
            T = generate_T_symmetric(level, deg, frac=False)
        else:
            T = generate_T(level, deg, frac=False)
    elif isinstance(T, (tuple)):
        print('Using preloaded monomial values.')
        filename, arr = T
        T = np.load(filename, allow_pickle=False)[arr]  
        
    edge_indices = []
    for i in range(3**(level + 1)):
        addr = address_from_index(level, i + 1)
        addr = ''.join(str(int(x)) for x in reversed(addr))
        digits = set(addr)
        if digits <= {'1', '2'}:
            edge_indices.append(i)

    edge_array = T[k, edge_indices, :]

    num_points, max_deg_plus_1 = edge_array.shape
    x_vals = range(num_points)

    for deg in range(max_deg_plus_1):
        plt.figure()  # <-- new pop-up window
        plt.plot(x_vals, edge_array[:, deg], marker='o', markersize=2)
        plt.title(f"Bottom — Monomial Degree {deg}")
        plt.xlabel("Index along edge")
        plt.ylabel(f"P_{deg}(x)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()



def monomial_right_edge(deg, k, level=7, T=None, symm=False):
    '''
    Args: 
    deg - Maximum degree monomial required
    k - Type of Monomial (k = 1, 2, 3)
    level - The level we would like to plot each monomial
    T - array of monomial values at the required level and degree or 
        tuple of (filename of .npz/.npy file containing this array , array name key string)
    symm - Boolean representing whether or not the fully symmetric orthogonal polynomials are needed

    Returns: 
    Plot of the right edge of symmetric and anti symmetric monomials
    '''
    k = k - 1

    if T is None:
        print('Generating array of monomial values. This may take some time...')
        if symm:
            T = generate_T_symmetric(level, deg, frac=False)
        else:
            T = generate_T(level, deg, frac=False)
    elif isinstance(T, (tuple)):
        print('Using preloaded monomial values.')
        filename, arr = T
        T = np.load(filename, allow_pickle=False)[arr]  

    edge_indices = []
    for i in range(3**(level + 1)):
        addr = address_from_index(level, i + 1)
        addr = ''.join(str(int(x)) for x in reversed(addr))
        digits = set(addr)
        if digits <= {'0', '2'}:
            edge_indices.append(i)
    
    edge_array = T[k, edge_indices, :]

    num_points, max_deg_plus_1 = edge_array.shape
    x_vals = range(num_points)

    for deg in range(max_deg_plus_1):
        plt.figure()  # <-- new pop-up window
        plt.plot(x_vals, edge_array[:, deg], marker='o', markersize=2)
        plt.title(f"Right — Monomial Degree {deg}")
        plt.xlabel("Index along edge")
        plt.ylabel(f"P_{deg}(x)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def op_left_edge(deg, k, level, normalized=False, lam=np.array([1]), frac=True):
    '''
    Args:
        n: Maximum degree of orthogonal polynomial.
        k: family of monomials to use in Gram-Schmidt (k = 1, 2, or 3)
        normalized: Boolean representing whether the resulting polynomials 
            should be normalized or monic.
        lam: np.array of lambda values for the generalized Sobolev inner 
            product. The default value is 1 (corresponding to the regular 
            Sobolev inner product). If lam = np.array([0]), 
            this is the L2 inner product.
        frac: Boolean representing whether the coefficients should remain as fractions or should be
        converted to floating point numbers at the end of all calculations.

    Returns:
        Plot of the left edge of symmetric and anti symmetric polynomials
    '''
    T = eval_op(deg, k, level, None, True, None, False)
    float_T = [[float(x) for x in row] for row in T]
    edge_indices = []

    for i in range(3**(level + 1)):
        addr = address_from_index(level, i + 1)
        addr = ''.join(str(int(x)) for x in reversed(addr))
        digits = set(addr)
        if digits <= {'0', '1'}:
            edge_indices.append(i)
    
    edge_array = T[:, edge_indices]

    max_deg_plus_1, num_points = edge_array.shape
    x_vals = range(num_points)

    for deg in range(max_deg_plus_1):
        plt.figure()  # <-- new pop-up window
        plt.plot(x_vals, edge_array[deg, :], marker='o', markersize=2)
        plt.title(f"Left — Polynomial Degree {deg}")
        plt.xlabel("Index along edge")
        plt.ylabel(f"P_{deg}(x)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        


def op_bottom_edge(deg, k, level, normalized=False, lam=np.array([1]), frac=True):
    '''
    Args:
        n: Maximum degree of orthogonal polynomial.
        k: family of monomials to use in Gram-Schmidt (k = 1, 2, or 3)
        normalized: Boolean representing whether the resulting polynomials 
            should be normalized or monic.
        lam: np.array of lambda values for the generalized Sobolev inner 
            product. The default value is 1 (corresponding to the regular 
            Sobolev inner product). If lam = np.array([0]), 
            this is the L2 inner product.
        frac: Boolean representing whether the coefficients should remain as fractions or should be
        converted to floating point numbers at the end of all calculations.

    Returns:
        Plot of the bottom edge of symmetric and anti symmetric polynomials
    '''
    T = eval_op(deg, k, level, None, True, None, False)
    float_T = [[float(x) for x in row] for row in T]
    edge_indices = []

    for i in range(3**(level + 1)):
        addr = address_from_index(level, i + 1)
        addr = ''.join(str(int(x)) for x in reversed(addr))
        digits = set(addr)
        if digits <= {'1', '2'}:
            edge_indices.append(i)
    
    edge_array = T[:, edge_indices]

    max_deg_plus_1, num_points = edge_array.shape
    x_vals = range(num_points)

    for deg in range(max_deg_plus_1):
        plt.figure()  # <-- new pop-up window
        plt.plot(x_vals, edge_array[deg, :], marker='o', markersize=2)
        plt.title(f"Bottom — Polynomial Degree {deg}")
        plt.xlabel("Index along edge")
        plt.ylabel(f"P_{deg}(x)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def op_right_edge(deg, k, level, normalized=False, lam=np.array([1]), frac=True):
    '''
    Args:
        n: Maximum degree of orthogonal polynomial.
        k: family of monomials to use in Gram-Schmidt (k = 1, 2, or 3)
        normalized: Boolean representing whether the resulting polynomials 
            should be normalized or monic.
        lam: np.array of lambda values for the generalized Sobolev inner 
            product. The default value is 1 (corresponding to the regular 
            Sobolev inner product). If lam = np.array([0]), 
            this is the L2 inner product.
        frac: Boolean representing whether the coefficients should remain as fractions or should be
        converted to floating point numbers at the end of all calculations.

    Returns:
        Plot of the right edge of symmetric and anti symmetric polynomials
    '''
    T = eval_op(deg, k, level, None, True, None, False)
    float_T = [[float(x) for x in row] for row in T]
    edge_indices = []

    for i in range(3**(level + 1)):
        addr = address_from_index(level, i + 1)
        addr = ''.join(str(int(x)) for x in reversed(addr))
        digits = set(addr)
        if digits <= {'0', '2'}:
            edge_indices.append(i)
    
    edge_array = T[:, edge_indices]

    max_deg_plus_1, num_points = edge_array.shape
    x_vals = range(num_points)

    for deg in range(max_deg_plus_1):
        plt.figure()  # <-- new pop-up window
        plt.plot(x_vals, edge_array[deg, :], marker='o', markersize=2)
        plt.title(f"Right — Polynomial Degree {deg}")
        plt.xlabel("Index along edge")
        plt.ylabel(f"P_{deg}(x)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

