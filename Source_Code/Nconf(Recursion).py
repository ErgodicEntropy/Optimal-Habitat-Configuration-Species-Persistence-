import numpy as np
import random
import matplotlib.pyplot as plt


def decomp(na, nr, nc):
    if nc == 1:
        if nr > na:
            return 1
        else:
            return 0
    ways = 0
    for i in range(na + 1): ways += decomp(na - i, nr, nc - 1)
    return ways


def mapper(x):
    return decomp(x,15,15)


x = np.array([random.randint(60,100) for k in range(30)])
y = list(map(mapper,x))

plt.scatter(x,y)
plt.show()


