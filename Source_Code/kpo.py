import numpy as np
from scipy.integrate import quad
import random

def computeintegrale(D, r, f):

    def integrand_num(x, y):
        return D * (np.gradient(f(x, y))**2) - r*(f(x, y)**2)


    def integrand_den(x, y):
        return f(x, y)**2


    numerator, _ = quad(integrand_num, 0, 1, 0, 1)
    denominator, _ = quad(integrand_den, 0, 1, 0, 1)
    S = numerator / denominator



def generate_function():

  operators = ['+', '-', '*', '/']

  operands = [str(random.randint(-10, 10)) for i in range(5)]

  random.shuffle(operands)
  random.shuffle(operators)

  function_string = operands[0]
  for i in range(1, 5):
    function_string += f" {operators[i-1]} {operands[i]}"
  return function_string


function = generate_function()
print(function)


def eigenvalue(n_iter):
    L = []
    for k in range(n_iter):
        L.append(computeintegrale(D, r, generate_function()))
    return np.min(L)







