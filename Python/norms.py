from math import gcd
import copy
class Fraction:
    def __init__(self, num, den):
        self.numer = num
        self.denom = den

    def __str__(self):
        self.simplify()
        return f"{self.numer}/{self.denom}"
    
    def simplify(self):
        my_gcd = gcd(self.numer, self.denom)
        self.numer = round(self.numer/my_gcd)
        self.denom = round(self.denom/my_gcd)
        if(self.denom < 0):
            self.numer = -self.numer
            self.denom = -self.denom
        return self

    def plus(self, frac):
        placehold = Fraction(1, 1)
        placehold.numer = (self.numer * frac.getDenom() + self.denom * frac.getNumer())
        placehold.denom = (self.denom * frac.getDenom())
        placehold.simplify()
        return placehold
    
    def minus(self, frac):
        placehold = Fraction(1, 1)
        placehold.numer = (self.numer * frac.getDenom() - self.denom * frac.getNumer())
        placehold.denom = (self.denom * frac.getDenom())
        placehold.simplify()
        return placehold
    
    def times(self, frac):
        placehold = Fraction(1, 1)
        placehold.numer = (self.numer * frac.getNumer())
        placehold.denom = (self.denom * frac.getDenom())
        placehold.simplify()
        return placehold
    
    def times(self, frac):
        placehold = Fraction(1, 1)
        placehold.numer = (self.numer * frac.getNumer())
        placehold.denom = (self.denom * frac.getDenom())
        placehold.simplify()
        return placehold
    
    def divide(self, frac):
        placehold = Fraction(1, 1)
        newFrac = frac.getReciprocal()
        placehold.numer = (self.numer * newFrac.getNumer())
        placehold.denom = (self.denom * newFrac.getDenom())
        placehold.simplify()
        return placehold
    
    def getReciprocal(self):
        return Fraction(self.denom, self.numer).simplify()
    
    def toString(self):
        string = ""
        string += str(self.numer)
        string += " / "
        string += str(self.denom)
        return string
    
    def getNumer(self):
        return self.numer
    
    def getDenom(self):
        return self.denom
    
    def toDecimal(self):
        return self.numer/self.denom

zero = Fraction(0,1)
one = Fraction(1,1)
half = Fraction(1,2)

def calculate_alfas(num_iterations):
    alfa0 = Fraction(1, 1)
    alfa1 = Fraction(1, 6)
    alfa = [alfa0, alfa1]
    for j in range(2, num_iterations + 1):
        sum = Fraction(0, 1)
        for l in range(1, j):
            sum = sum.plus(alfa[l].times(alfa[j - l]))
        new_alfa = Fraction(4, (5**j) - 5)
        new_alfa = new_alfa.times(sum)
        alfa.append(new_alfa)
    return alfa

def calculate_betas(num_iterations, alfa):
    beta0 = Fraction(-1, 2)
    beta = [beta0]
    for j in range(1, num_iterations + 1):
        sum = Fraction(0, 1)
        for l in range(0, j):
            sum_of_powers = 3*(5**(j - l)) - (5**(l + 1)) + 6
            sum = sum.plus(beta[l].times(alfa[j - l].times(Fraction(sum_of_powers, 1))))
        new_beta = Fraction(2, 15*((5**j) - 1))
        new_beta = new_beta.times(sum)
        beta.append(new_beta)
    return beta

def calculate_etas(num_iterations, alfa, beta):
    eta0 = Fraction(0, 1)
    eta = [eta0]
    for j in range(1, num_iterations + 1):
        sum = Fraction(0, 1)
        for l in range(0, j):
            sum = sum.plus(eta[l].times(beta[j - l]))
        sum.numer = 2*sum.numer
        new_eta = Fraction((5**j) + 1, 2)
        new_eta = new_eta.times(alfa[j])
        new_eta = new_eta.plus(sum)
        eta.append(new_eta)
    return eta

def inner_productP(j, a, k, b, greeks):
    alfa = greeks[0]
    beta = greeks[1]
    eta = greeks[2]
    alfa_ = greeks[3]
    m_ = min(j, k)
    sum = Fraction(0, 1)
    if a == 1 and b == 1:
        for l in range(j - m_, j + 1):
            newTerm = alfa[j - l].times(eta[k + l + 1])
            newTerm = newTerm.minus(alfa[k + l + 1].times(eta[j - l]))
            sum = sum.plus(newTerm)
        sum = sum.times(Fraction(2, 1))

    if a == 2 and b == 2:
        for l in range(j - m_, j + 1):
            newTerm = beta[j - l].times(alfa_[k + l + 1])
            newTerm = newTerm.minus(beta[k + l + 1].times(alfa_[j - l]))
            sum = sum.plus(newTerm)
        sum = sum.times(Fraction(2, 1))

    if a == 3 and b == 3:
        for l in range(j - m_, j + 1):
            newTerm = alfa[j - l + 1].times(eta[k + l + 2])
            newTerm = newTerm.minus(alfa[k + l + 2].times(eta[j - l + 1]))
            sum = sum.plus(newTerm)
        sum = sum.times(Fraction(18, 1))

    if a == 1 and b == 2:
        for l in range(0, j + 1):
            newTerm = alfa[j - l].times(alfa_[k + l + 1]) 
            newTerm = newTerm.minus(beta[k + l + 1].times(eta[j - l]))
            sum = sum.plus(newTerm)
        sum = sum.times(Fraction(2, 1))
    return sum

def generate_IPvals(num):
    alphas = calculate_alfas(2*num)
    betas = calculate_betas(2*num, alphas)
    etas = calculate_etas(2*num, alphas, betas)
    alpha_prime = copy.deepcopy(alphas)
    for i in range(len(alpha_prime)):
        alpha_prime[i] = alpha_prime[i].times(Fraction(-1, 1))
    alpha_prime[0] = Fraction(-1,2)

    greeks = [alphas, betas, etas, alpha_prime]
    inner_products11 = []
    inner_products12 = []
    inner_products22 = []
    for i in range(num):
        level11 = []
        level12 = []
        level22 = []
        for j in range(num):
            level11.append(inner_productP(i, 1, j, 1, greeks).simplify())
            level12.append(inner_productP(i, 1, j, 2, greeks).simplify())
            level22.append(inner_productP(i, 2, j, 2, greeks).simplify())
        inner_products11.append(copy.deepcopy(level11))
        inner_products12.append(copy.deepcopy(level12))
        inner_products22.append(copy.deepcopy(level22))
    
    return inner_products11, inner_products12, inner_products22

def adv_IP(array1, array2):

    ## assumes standard representation, in the form of [P01, P02, P11, P12, ...]

    array1 = copy.deepcopy(array1)
    array2 = copy.deepcopy(array2)

    inner_products11, inner_products12, inner_products22 = generate_IPvals(max(len(array1), len(array2))//2 + 1)

    sum = Fraction(0,1)

    for i in range(len(array1)):
        for j in range(len(array2)):
            if i % 2 == 0:
                if j % 2 == 0:
                    sum = sum.plus(array1[i].times(array2[j].times(inner_products11[i//2][j//2])))
                else:
                    sum = sum.plus(array1[i].times(array2[j].times(inner_products12[i//2][j//2])))
            else:
                if j % 2 == 0:
                    sum = sum.plus(array1[i].times(array2[j].times(inner_products12[j//2][i//2])))
                else:
                    sum = sum.plus(array1[i].times(array2[j].times(inner_products22[i//2][j//2])))
    
    return sum

def generate_OP(num):

    """
    Generates the orthogonal polynomials as a linear combination of \{P_{j,k}\}
    
    Input:
    - num: the length of the orthogonal polynomials to be generated
    """

    inner_products11, inner_products12, inner_products22 = generate_IPvals(num)

    ## Initialize a 2-D array consisting of the orthogonal polynomials
    ## Note: Each p_{j,k} will be represented as a linear combination of the P_{j,k}s
    ortho_poly = []

    ## Iterate the specified number of times
    for i in range(num):

        ## Initialize it so that P_{j,k} has coefficient 1
        expansion = []
        for j in range(num):
            expansion.append(Fraction(0,1))
        expansion[i] = Fraction(1,1)    # expansion is P_{j//2,j%2}
        
        for j in range(i):
            poly_sum = copy.deepcopy(ortho_poly[j]) # poly_sum is p_{j//2.j%2}

            ## Need to renormalize each time that an inner product is taken
            norm2 = adv_IP(poly_sum, poly_sum)
            # print("\n\nNORM: "+str(norm2)+"\n\n")

            ## Calculate the coefficient - inner product of P_{j//2,j%2}
            coef = Fraction(0,1)
            coef = adv_IP(expansion, poly_sum)
    
            # THIS COMMENTED SEGMENT OF CODE THIS PROBABLY WRONG
            # for idx in range(len(poly_sum)):
            #     if j % 2 == 0:
            #         if idx % 2 == 0:
            #             coef = coef.plus(poly_sum[idx].times(inner_products11[j//2][idx//2]))
            #         else:
            #             coef = coef.plus(poly_sum[idx].times(inner_products12[j//2][idx//2]))
            #     else:
            #         if idx % 2 == 0:
            #             coef = coef.plus(poly_sum[idx].times(inner_products12[idx//2][j//2]))
            #         else:
            #             coef = coef.plus(poly_sum[idx].times(inner_products22[j//2][idx//2]))

            # print("ortho " + str(j) + ", mono " + str(i))
            # print("coef " + coef.toString())
            # print("coefnew " + coef_new.toString())
                
            coef = coef.divide(norm2)

            for idx in range(len(poly_sum)):
                expansion[idx] = expansion[idx].minus(coef.times(poly_sum[idx]))

        ortho_poly.append(expansion)
                
    return ortho_poly

print(generate_OP(1))
            
alphas = calculate_alfas(30)
betas = calculate_betas(30, alphas)
etas = calculate_etas(30, alphas, betas)
alpha_prime = copy.deepcopy(alphas)
for i in range(len(alpha_prime)):
    alpha_prime[i] = alpha_prime[i].times(Fraction(-1, 1))
alpha_prime[0] = Fraction(-1,2)
greeks = [alphas, betas, etas, alpha_prime]       

# for i in range(15):
#     print(inner_productP(i, 1, i, 2, greeks))

# # 
orthopoly = generate_OP(33)
for i in range(len(orthopoly)):
    toPrint = ""
    for j in range(len(orthopoly[i])):
        toPrint+=Fraction.toString(orthopoly[i][j]) + "   "
    print(toPrint)
    norm2 = adv_IP(orthopoly[i], orthopoly[i])
    print("Polynomial " + str(i) + " Norm Squared  " + "Fractional: " + norm2.toString() + " " + "Decimal:" + str(norm2.getNumer()/norm2.getDenom())+"\n\n")

# my_num = 10
# alfa = calculate_alfas(my_num)
# beta = calculate_betas(my_num, alfa)
# eta = calculate_etas(my_num, alfa, beta)
# alfa_ = alfa
# alfa_[1] = Fraction(-1, 2)
# greeks = [alfa, beta, eta, alfa_]

# frac1 = Fraction(-53, 90)
# frac2 = Fraction(-48551 ** 2, 48600 ** 2)
# print(frac1.plus(frac2).simplify())



# print(inner_productP(0, 1, 0, 2, greeks))


# poly1 = [[one,zero,zero, one], [one,one,zero, one], [one,half,zero, one, one, one], [zero, zero, one, half, zero, one]]
# poly2 = [[zero,one,half,zero], [zero, half, zero, one], [zero, zero, zero, one, one], [one, zero , half]]
# for i in range(len(poly1)):
#     p01norm = adv_IP(poly1[i], poly1[i])
#     p02norm = adv_IP(poly2[i], poly2[i])
#     p01p02ip = adv_IP(poly1[i], poly2[i])
#     print(p01norm)
#     print(p02norm)
#     print(p01p02ip)
#     print("Cauchy Schwartz " + str((p01norm.times(p02norm)).toDecimal() >= p01p02ip.times(p01p02ip).toDecimal()))
#     print("Postivity " + str(p01norm.toDecimal() >= 0 and p02norm.toDecimal() >= 0))




print(adv_IP([zero, one], [zero, one]))
print(adv_IP([one, zero], [zero, one]))

# print("Alphas")
# for i in range(10):
#     print("alpha_" + str(i) + " = " + alphas[i].toString())
# print("\n\n")
# print("Betas")
# for i in range(10):
#     print("beta_" + str(i) + " = " + betas[i].toString())
# print("\n\n")
# print("Etas")
# for i in range(10):
#     print("eta_" + str(i) + " = " + etas[i].toString())
# print("\n\n")
