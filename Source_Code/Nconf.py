import numpy as np
import random
import matplotlib.pyplot as plt


#method1
def GenComb(n,nc,nr,n_iter,Monte_n_iter):
    MntCarloN = 0
    for k in range(Monte_n_iter):
        N = 0
        for j in range(n_iter):
            S = 0
            L = [random.randint(0,nr) for i in range(nc)]
            for k in range(len(L)):
                S+=L[k]
            if n == S:
                N+=1
        MntCarloN+=N/Monte_n_iter
    return int(MntCarloN)


def mapper(x):
    return GenComb(x,15,15,1000,1000)


x = np.array([random.randint(70,170) for k in range(50)])
y = list(map(mapper,x))

plt.scatter(x,y)
plt.show()



#method2
#def summ(A):
    #G = 0
    #for k in range(len(A)):
     #   G+=A[k]
    #return G

#def GenSel(n,nc,nr,n_iter):
    #F = []
    #for k in range(n_iter):
     #   L = [random.randint(0,nr) for i in range(nc)]
      #  F.append(L)

    #X = list(filter(lambda x: summ(x) == n,F))
    #return len(X)



