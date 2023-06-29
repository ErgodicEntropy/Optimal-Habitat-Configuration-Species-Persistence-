import random
import numpy as np
import math

def draw_grid(n,nr,nc,g): #n is n+ in the article
  # Create a grid of all white squares
  grid = [['.' for i in range(nr)] for j in range(nc)]

  # Randomly select n squares to be shaded black (habitat) symbolized as #
  L = [[]]
  for i in range(n):
    x = random.randint(0, nr-1)
    y = random.randint(0, nc-1)
    if [x,y] != L[i]:
        L.append([x,y])
        grid[x][y] = g
    else:
      while [x,y] == L[i]:
        x = random.randint(0, nr-1)
        y = random.randint(0, nc-1)
      L.append([x,y])
      grid[x][y] = g

  return grid

def print_grid(grid):
  for row in grid:
    for square in row:
      print(square, end=' ')
    print()


def Habitat_Abundance(n,nr,nc): #h
  return n/nr*nc

def Habitat_Index(grid):
    H = [[]]
    S = 0
    for row in grid:
        for k in range(len(grid)):
          if row[k]=='#':
            if [grid.index(row),k] != H[S]:
              H.append([grid.index(row),k])
              S+=1

    H.remove([])
    return H


def Empty_Index(grid):
    E = [[]]
    S = 0
    for row in grid:
        for k in range(len(grid)):
          if row[k]=='.':
            if [grid.index(row),k] != E[S]:
              E.append([grid.index(row),k])
              S+=1

    E.remove([])
    return E


#So far, we have only randomly generated the habitat n+ on our space without taking in consideration the Fisher-Kolmogorov dynamics.

#The following two functions set the stage for incorporating the F-K equation dynamics ie; diffusion and reaction separately.

def diffusivity(grid, n, D):#We model the diffusion phenomenon as a random walk with step proportional to D
  G = Habitat_Index(grid)
  for k in range(len(G)):
      grid[G[k][0]][G[k][1]] = '.'
      if G[k][0] - D >= 0  and G[k][0] + D <= len(grid):
          G[k][0]+= random.choice([-D,D])
      if G[k][1] - D >= 0 and G[k][1] + D <= len(grid):
          G[k][1]+= random.choice([-D,D])
      grid[G[k][0]][G[k][1]]= '#'
  return grid


def growth_rate(grid,nc,nr,n,b,m):#nu = growth rate = birth rate - mortality rate (b-m)
  G = Habitat_Index(grid)
  E = Empty_Index(grid)
  if b-m == 0:
      pass
  if b-m > 0:
    for k in range(b): # b is necessarily smaller than or equal to nc*nr - n
      grid[E[random.randint(0,nc*nr-n)][0]][E[random.randint(0,nc*nr-n)][1]] = '#'
  if b-m < 0:
    for s in range(m):# m is necessarily smaller than or equal to n
      grid[G[random.randint(0,n)][0]][G[random.randint(0,n)][1]] = '.'
  return grid

def crowd_rate(grid,nc,nr):
  pass

mod = 1000000007

#Code block for Nconf
def calculate(pos, left, k, L, R):

	# Base Case
	if (pos == k):
		if (left == 0):
			return 1
		else:
			return 0

	# If N is divides completely
	# into less than k groups
	if (left == 0):
		return 0

	answer = 0

	# Put all possible values
	# greater equal to prev
	for i in range(L, R + 1):
		if (i > left):
			break
		answer = (answer +
				calculate(pos + 1,
							left - i, k, L, R)) % mod
	return answer

# Function to count the number of
# ways to divide the number N
def Nconf(n, k, L, R):
	return calculate(0, n, k, L, R)


def move_left(grid,nc,nr):
   #Shift all the squares in each row to the left
  for i in range(nr):
    for j in range(1,nc):
        if grid[i][j] == '#' and grid[i][j-1] != '#':
            grid[i][j-1] = grid[i][j]
            grid[i][j] = '.'

def move_right(grid,nc,nr):
   #Shift all the squares in each row to the right
  for i in range(nr-4):
    for j in range(nc-1):
        if grid[i][j] == '#' and grid[i][j+1] != '#':
            grid[i][j+1] = grid[i][j]
            grid[i][j] = '.'


def move_down(grid,nc,nr):
   #Shift all the squares in each column to the down
  for i in range(nr-1):
    for j in range(nc):
        if grid[i][j] == '#' and grid[i+1][j] != '#':
            grid[i+1][j] = grid[i][j]
            grid[i][j] = '.'

def reduce(grid,nc,nr):
      for j in range(nr*nc):
        move_down(grid,nc,nr)
        move_left(grid,nc,nr)
      return grid

def Multiply(nc,nr):
  for k in range(Nconf(5,nc,0,nr)-1):
    S = draw_grid(150,nr,nc,'#')
    F = reduce(S,nc,nr)
    print_grid(F)
    print(clustering_distance(S))




def clustering_distance(grid): #Based off cluster analysis method in Machine Learning
  G = Habitat_Index(grid)
  F = []
  for i in range(len(G)):
    distances = []
    for j in range(len(G)):
      if j != i:
        x1, y1 = G[i]
        x2, y2 = G[j]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        distances.append(distance)
    F.append(np.sum(distances)/len(distances))
  return np.sum(F)/len(F)


         #Such distance is inversely proportional to connectedness, and therefore to persistence

gridd = draw_grid(150, 20, 20,'#')
print("Before Rearrangement")
print_grid(gridd)
print(clustering_distance(gridd))
print('\n',end= '')

print("After Rearrangement")

R = reduce(gridd,20,20)

print_grid(R)
print(clustering_distance(R))

Multiply(20,20)












#The gist of the code is based off cluster analysis. The type of clustering used to measure persistence is hierarchical clustering. We assume that connectivity brings about persistence although the literature is pretty complex on that matter (sometimes the opposite is true; habitat fragmentation brings about species persistences). Hierarchical clustering is different from other clustering models in the sense that it capitalizes upon connectivity as a criterion for grouping objecs (in our case; habitat) together.

#the literature suggests that habitat fragmentation is detrimental to species persistence (but not biodiversity) in the case of single-species models which is the case here. This is numerically clear in the value of the clustering distance = f(connectivity,n) a decreasing function with respect to both variables (with respect to n thanks to single-species model)



#Principle of maximum entropy: the trick used to generate the Nconf connected configurations from the same randomly generated configuration is based off the principle of maximum entropy. In other words, there is a statistical equivalence (not analytical ie; one requiring the law of the large number) between the case 1: generate one random configuration and then generate Nconf connected/aggregated configurations from it, and case 2: produce a connected/aggregated configuration for each randomly generated configuration.

#This can also be termed in set-theoretic language manifested in the non-injective nature of the reduce map.

#Law of large numbers

#Nconf loses its combinatorial significance once we rely on principle of maximum entropy