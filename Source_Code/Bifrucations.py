import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage, misc

def bifurcation_plot(f,f_x,r,x,rlabel='r'):
    """ produce a bifurcation diagram for a function f(r,x) given
        f and its partial derivative f_x(r,x) over a domain given by numpy arrays r and x

        f(r,x)  :  RHS function of autonomous ode dx/dt = f(r,x)
        f_x(r,x):  partial derivative of f with respect to x
        r       :  numpy array giving r coordinates of domain
        x       :  numpy array giving x coordinates of domain
        rlabel  :  string for x axis parameter label
    """
    # set up a mesh grid and extract the 0 level set of f
    R,X = np.meshgrid(r,x)
    plt.figure()
    CS = plt.contour(R,X,f(R,X),[0],colors='k')
    plt.clf()

    c0 = CS.collections[0]
    # for each path in the contour extract vertices and mask by the sign of df/dx
    for path in c0.get_paths():
        vertices = path.vertices
        vr = vertices[:,0]
        vx = vertices[:,1]
        mask = np.sign(f_x(vr,vx))
        stable = mask < 0.
        unstable = mask > 0.

        # plot the stable and unstable branches for each path
        plt.plot(vr[stable],vx[stable],'b')
        #plt.hold(True)
        plt.plot(vr[unstable],vx[unstable],'b--')

    plt.xlabel('parameter {0}'.format(rlabel))
    plt.ylabel('x')
    plt.legend(('stable','unstable'),loc='best')
    plt.xlim(r[0],r[-1])
    plt.ylim(x[0],x[-1])

f = lambda r,x:  x*(r-x)
f_x = lambda r,x: r- 2.*x

x = np.linspace(0,4,100)
r = np.linspace(-4,4,100)

bifurcation_plot(f,f_x,r,x)
plt.show()

#https://ipython-books.github.io/121-plotting-the-bifurcation-diagram-of-a-chaotic-dynamical-system/