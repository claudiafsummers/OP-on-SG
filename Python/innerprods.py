import numpy as np
from fractions import Fraction

from recursions import alpha, beta, gamma, eta, ap


'''
This file contains functions used to compute the L2 inner product 
between the monomial baisis P_jk. The algorithms for computing the inner 
products are derived from the Kasso, Tuley paper OP on SG.

There are some slight corrections to the algorithms mentioned in the 
paper that are implemented here.

'''


def inner0_j1k1(j, k):
    '''
    Calculates the L2 inner product <P_j1, P_k1>

    Args:
        j, k: indices for the monomials P_j1, P_k1

    Returns:
        L2 inner product <P_j1, P_k1>

    '''

    ms = min(j, k)
    s1 = 0
    for l in range(j-ms, j+1):
        s1 += alpha(j-l)*eta(k+l+1) - alpha(k+l+1)*eta(j-l)
    return 2*s1



def inner0_j2k2(j, k):
    '''
    Calculates the L2 inner product <P_j2, P_k2>

    Args:
        j, k: indices for the monomials P_j2, P_k

    Returns:
        L2 inner product <P_j2, P_k2>
    '''
    ms = min(j, k)
    s1 = 0
    for l in range(j-ms, j+1):
        s1 += beta(j-l)*ap(k+l+1) - beta(k+l+1)*ap(j-l)
    return 2*s1



def inner0_j3k3(j, k):
    '''
    Calculates the L2 inner product <P_j3, P_k3>

    Args:
        j, k: indices for the monomials P_j3, P_k3

    Returns:
        L2 inner product <P_j3, P_k3>
    '''
    ms = min(j, k)
    s1 = 0
    for l in range(j-ms, j+1):
        s1 += alpha(j-l+1)*eta(k+l+2) - alpha(k+l+2)*eta(j-l+1)
    return 18*s1



def inner0_j1k2(j, k):
    '''
    Calculates the L2 inner product <P_j1, P_k2>

    Args:
        j, k: indices for the monomials P_j1, P_k2

    Returns:
        L2 inner product <P_j1, P_k2>

    '''
    s1 = 0
    for l in range(j+1):
        s1 += alpha(j-l)*ap(k+l+1) + beta(k+l+1)*eta(j-l)
    return 2*s1


# This function is used to symmetrize an upper triangular matrix.
# This function is used when creating Gram Matrices for the inner products.ArithmeticError
def symmetrize(arr):
    #return arr + arr.T - arr.multiply_elementwise(eye(arr.rows))
    return arr + arr.T - np.diag(np.diag(arr))



# This function takes a list/array of integers and outputs the concatenation of the integers

def lis2str(lis):
    '''
    Convert a list of integers to an integer string using concatenation.

    Args:
        lis: list or np.array of integers

    Returns:
        a string which is the concatenation of the numbers in lis

    Example:
        lis2str(np.array([1, 2, 3]))
        >> '123'
        lis2str([012, 345, 678])
        >> '012345678'
    '''
    return ''.join(str(int(x)) for x in lis)


# The L2 inner products <P_j1, P_k3> and <P_j2, P_k3> are 0
def inner0_j1k3(j, k): return 0


def inner0_j2k3(j, k): return 0

'''
This is a dictionary mapping the values (i, i') to the L2 inner product 
    function for <P_ji, P_ki'>. This dictionary is used in the 
    construction of the Polynomial class.
'''
inner_dict = {(1, 1): inner0_j1k1, (2, 2): inner0_j2k2, (3, 3): inner0_j3k3,
              (1, 2): inner0_j1k2, (1, 3): inner0_j1k3, (2, 3): inner0_j2k3}


'''
vals_dict maps the values 1, 2, 3 to the functions alpha, beta, and 
    gamma. This dictionary, along with norm_dict are used in the computation 
    of the values and normal derivatives of the polynomials P_jk (k = 1, 2, 3) 
    on the boundary of SG. The functions are based on the Kasso, Tuley paper.

'''
vals_dict = {1: alpha, 2: beta, 3: gamma}


def dnpj2(j): return -alpha(j)


def dnpj3(j): return 3*eta(j+1)


norm_dict = {1: eta, 2: dnpj2, 3: dnpj3}

# Beginning to code the coeffs of the 6-term recursion formula from REU research
# Following array holds the polynomial norm^2 values of OP until degree 15
W_og = [Fraction(1,1), Fraction(1,90), Fraction(1,4860), Fraction(449,813564000), Fraction(239,368849578500), 
     Fraction(2066368051665377, 629048898301472861988061184), Fraction(3545305403327543, 23767377061348129437985445773312), Fraction(6718809449072715, 786923746760081776954992465281024), Fraction(1183044123656707, 106668296892892058816570517611255693312), Fraction(2860745664609161, 238856098112592540348293218038097903616), 
     Fraction(9627056256209, 12196447062940456644902380374159820595396608), Fraction(3851328387896429, 3796506500124413877691328092804134258541068288), Fraction(4716600399425893, 10028081567650401763334319959642118923626497148190720), Fraction(5788106412822953, 602653888766169205626167898313274618392951996284928), Fraction(-6137659903419413, 5677929472173771931701743587307455821072495851207655424), 
     Fraction(4204044999261969, 9827065874245036815040782972853810055398061944730550272), Fraction(-3271151404598261, 923933958290821519907220147878080287158452708353595408384), Fraction(3255843246923451, 169390274376970880083620384024279643385307767399720708785307648), Fraction(2662466997717923, 15909432149392300232461096616312514199218250951740559194062848), Fraction(7367078417191885, 282207861138771686302447533037061669291586899961786098992326715113472),
     Fraction(-5672490084829005, 26188105209092837887346745516377894887629316745975363043174907904), Fraction(-647635767819359, 12630454751117096211275533716515829657220274172229232708479176469905408), Fraction(1130887642807563, 3332200779972279563665915095862855158321136876061743948419603365888), Fraction(-7688203683525217, 35292804953066030162794703894648263299357486763476614851844473450569377251328), Fraction(387218724264737, 1680405839986367881145858844369321166181843952785495296729556960935936),
     Fraction(879586162864723, 27628691778185534349279750651260871723447604017168125680898780443326327228989440), Fraction(5787240296572883, 117559620271414585450368664605709614051863122691663605255477789558575202304), Fraction(-1291869452530723, 4118107379187763322026914891729281445914505565322724616820380029779160288468567851008), Fraction(2706324314515601, 6783453648643325537616972265248497434591417211498076106233759862842072236032), Fraction(-8812968288510413, 1294794844777738388890728010668022167373658873054586348171234715828445640918163318112256),
     Fraction(-1011466018588763, 23533325506375457335818925551956599317622268976870801575277430675129684197376), Fraction(-1056142743141251, 43959127741739749328933819267835372803890661570121780706070117918995687990826384496753901568), Fraction(31772160302935002130153472,  72329874514334090914724148514967335368309229764292757179981443795677038782243981534167040)
     ] # squared

def aj(j):
    '''
    This computes ||p_j,1||/||p_j-1,1||. Stores values in an array length j.
    '''
    y = []
    for i in range(1, j+1):
        a = W_og[(2*i)]
        b = W_og[(2*(i-1))]
        c = np.sqrt(a/b)
        y.append(c)
    return y

def innerbj(j):
    '''
    Calculates the inner product <f_j+1,1, Q_j-1,2> 
    '''
    y = [] # add b_0 value here
    if j == 0:
        return y
    else:
        for i in range(1, j+1):
            a_0 = Fraction(<P_j-1,pj-1,1>,W_og[(2*(i-1))])
            a_1 = Fraction(<P_j,2,p_j,1>), W_og[(2*i)]) 
            a = -a_0 + a_1
            b_0 = np.sqrt(W_og[(2*i)])
            b_1 = np.sqrt(W_og[(2*(i-1))+1])
            b = b_0 * b_1
            c = Fraction(a,b)
            y.append(c)
            return y

def innercj(j):
    '''
    Calculates the inner product <f_j+1,1, Q_j,1> 
    '''

def innerdj(j):
    '''
    Calculates the inner product <f_j+1,1, Q_j,2> 
    Also computes c'_j (equal to d_j)
    '''
    y = [] 
    for i in range(j+1):
        a = inner <p_j,2,f_j+1,1>
        b = W_og[(2*i)] * W_og[(2*i)+1]
        c = Fraction(a,b)
        y.append(c)
    return y

def bj_prime(j):
    '''
    This computes ||p_j,2||/||p_j-1,2||. Stores values in an array length j.
    '''
    y = []
    for i in range(1, j+1):
        a = W_og[(2*(i))+1]
        b = W_og[(2*(i-1))+1]
        c = np.sqrt(a/b)
        y.append(c)
    return y 

def innerdj_prime(j):
    '''
    Calculates the inner product <f_j+1,2, Q_j,2> 
    '''

def innergj_prime(j):
    '''
    Calculates the inner product <f_j+1,2, Q_j+1,1> 
    b_j is equal to g'_j-1
    '''
    a = innerbj(j+1)
    y = a[1:]
    return y 
