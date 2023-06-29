import numpy as np
import matplotlib.pyplot as plt


def logistic(mu, u):
    return u * (1 - mu*u)

u = np.linspace(0, 1)
fig, ax = plt.subplots(1, 1)
ax.plot(u, logistic(2, u), 'k')

def plot_system(mu, u0, n, ax=None):
    # Plot the function and the
    # y=u diagonal line.
    t = np.linspace(0, 1)
    ax.plot(t, logistic(mu, t), 'k', lw=2)
    ax.plot([0, 1], [0, 1], 'k', lw=2)

    # Recursively apply y=f(u) and plot two lines:
    # (u, u) -> (u, y)
    # (u, y) -> (y, y)
    u = u0
    for i in range(n):
        y = logistic(mu, u)
        # Plot the two lines.
        ax.plot([u, u], [u, y], 'k', lw=1)
        ax.plot([u, y], [y, y], 'k', lw=1)
        # Plot the positions with increasing
        # opacity.
        ax.plot([u], [y], 'ok', ms=10,
                alpha=(i + 1) / n)
        u = y

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f"$mu={mu:.1f}, \, u_0={u0:.1f}$")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6),
                               sharey=True)
plot_system(2.5, .1, 10, ax=ax1)
plot_system(3.5, .1, 10, ax=ax2)

n = 10000
mu = np.linspace(2.5, 4.0, n)

iterations = 1000
last = 100

u = 1e-5 * np.ones(n)

plt.show()


#https://ipython-books.github.io/121-plotting-the-bifurcation-diagram-of-a-chaotic-dynamical-system/