#Pseudocode for the bounded case
import random
import math
from sympy import *

class domain:
    def __init__(self, L1, L2, n+, n-, L, K):
        self.L1 = L1
        self.L2 = L2
        self.n+ = n+
        self.n- = n-
        self.L = L #let L be a row boolean list such that L[n+][n+]=1 and L[n-][n-]=0 where len(L)= nc and Card(L)= nr
        self.K = K #let K be a column boolean list such that K[n+][n+]=1 and K[n-][n-]=0 where len(K)= nr and Card(K)= nc

#1- Discretization
    def discretize(L1, L2, G, F, nc, nr):
        for k in range(1,nc-1):
            G[k]= (k/nc-1)*L1
        for j in range(1,nr-1):
            F[j]= (j/nr-1)*L2       #Complexity = O(nc + nr)

    def classification(nc,nr):
        P = []
        N = ['n+', n-]
        for k in range(nc):
            for j in range(nr):
                P[j][k] = random.choice(N)
        for k in range(nc):
            for j in range(nr):
                if P[j][k] = n+:
                    L[j]k]=1
                else:
                    L[j][k]=0
        for j in range(nr):
            for k in range(nc):
                if P[j][k]= n+:
                    K[j][k]= 1
                else:
                    K[j][k]= 0      #Complexity = O(nc x nr)


#2-Reducing the search space:

        def moveleft(s,a):
            while a != 0:
                L[s][a-1]=L[s][a] #Complexity = O(nc-1)
        def movedown(b,c):
            while b != nr-1:
                K[b+1][c]= K[b][c] #Complexity = O(nr-1)


        def reduce(nr, nc, n+, P): #For each C there is a matrix representing it P
            for j in range(nr):    #For each C+ there is a matrix representing it P+
                for k in range(nc):
                    if P[j][k] == n+: #equivalent to saying L[j][k] == 1
                        moveleft(j,k)

            for m in range(nc):
                for v in range(nr):
                    if P[v][m] == n+: #equivalent to saying K[v][m] == 1
                        movedown(v,m)

        return P+* = reduce(nr, nc, n+ P)
        #the purpose of this reduce block of code is to triangulize inferior P+
                                   #Complexity = O(nr x nc x card(Sh) x (nr+nc-2))

Sh* = set(reduce(nr, nc, n+, P) for i in range(math.comb(n+,n)))




#3-Brute-Force search lambda for all C+*(nr,nc)
    def bruteforce(P+*):
        eigenvalue(P+*) = "eigenvalue of P+*"
        def computeeigenv(P+*):
            return eigenvalue(P+*)
        OP = []
        for P+* in Sh*: #Sh* the set of habitat configurations C+*(nr,nc)
            y = computeeigenv(P+*)
            OP.append(y)

    return min(OP)      #Complexity = O(Card(Sh*))
    Sh*_ = filter(bruteforce, Sh*)

#4- interpolation (Reverse-Engineering): Taking nc, nr to the limit as they get arbitrarily large

nr = symbols('nr')
nc = symbols('nc')
distance = min(math.dist(P+*(nr,nc), Sh*_));

interpolation = limit(distance, nr,nc, oo)


#Global Complexity = O(nc+nr + Card(Sh*)+ nr x nc x card(Sh))





