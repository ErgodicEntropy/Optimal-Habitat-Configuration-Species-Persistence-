import numpy as np
from scipy.integrate import odeint
from matplotlib.pyplot import plot, xlabel, ylabel
import matplotlib.pyplot as plt

# parameters
r = 1.
K = 1.
D = 0.1
C = 0.5 #Allee threshold

# the size of the spatial domain
# his is actual size, such as "kilometres"
L = 50.
# the number of points in the grid
grid_size = 100
# the integration times
t = np.arange(0, 300, 0.1)
# the grid
dx = L / (grid_size+1)
grid = np.arange(0, L, dx)[1:-1]

# the initial condition, consisting of a small "square" in the middle
y0 = np.zeros_like(grid)
y0[grid_size//2 - 2:grid_size//2 + 2] = 0.1

# let's define the flux
def fkpp(y, t, r, K, D, dx):
    # we calculate the spatial second derivative
    d2x = -2 * y
    d2x[1:-1] += y[2:] + y[:-2]
    d2x[0] += y[1]
    d2x[-1] += y[-2]
    d2x = d2x/dx/dx
    # then add the reaction terms
    dy = r * y * (1. - y/K)*((y-C)/K) + D * d2x
    return dy

y = odeint(fkpp, y0, t, (r, K, D, dx))


for i in np.linspace(t[0], t[-1], 10):
    plot(grid, y[int(i),:])
xlabel('espace')
ylabel('densité de population')

plt.title('cas allee')
plt.show()

