import matplotlib.pyplot as plt
import numpy as np
import math



def comb(k):
    return math.comb(225, k)



x = np.array([0,1,5,7,11,15,19,25,30,42,49,54,66,75,85,98,101,103,105,107,109,112,113,114,115,116,117,118,119,120,121,125,130,138,140,148,157,164,170,178,186,193,200,209,215,220,224,225])
y = list(map(comb, x))


plt.scatter(x, y)
plt.title("Comb(n,n+) = entropie de Shannon/Gibbs")
plt.xlabel("n+")
plt.ylabel("Comb(n,n+)")
plt.show()





