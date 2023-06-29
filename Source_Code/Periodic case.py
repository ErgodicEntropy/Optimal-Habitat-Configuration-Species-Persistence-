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

def ReflectionX(grid):
  Rgrid_1 = [['.' for i in range(len(grid[0]))] for j in range(len(grid))]
  for x in range(len(grid[0])):
    for y in range(len(grid)):
      if grid[x][y] == '#':
        Rgrid_1[len(grid[0])-1-x][y] = '#'
  return Rgrid_1


def ReflectionY(grid):
  Rgrid_2 = [['.' for i in range(len(grid[0]))] for j in range(len(grid))]
  for x in range(len(grid[0])):
    for y in range(len(grid)):
      if grid[x][y] == '#':
        Rgrid_2[x][len(grid)-1-y] = '#'
  return Rgrid_2

def AggregateX(grid1,grid2):
  return grid1 + grid2


def AggregateY(grid1,grid2):
    gridC = [[]]
    for k in range(len(grid1)):
        gridC.append(grid1[k]+grid2[k])
    gridC.remove([])
    for row in gridC:
        for k in range(len(gridC[0])):
            print(row[k],end='')
        print()



def print_grid(grid):
  for row in grid:
    for square in row:
      print(square, end=' ')
    print()

def habitat_abundance(n,nr,nc): #h
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
      if G[k][0] - D >= 0  and G[k][0] + D <= len(grid[0]):
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




def move_left(grid,nc,nr):
   #Shift all the squares in each row to the left
  for i in range(nr):
    for j in range(1,nc):
        if grid[i][j] == '#' and grid[i][j-1] != '#':
            grid[i][j-1] = grid[i][j]
            grid[i][j] = '.'

def move_down(grid,nc,nr):
   #Shift all the squares in each column to the down
  for i in range(nr-1):
    for j in range(nc):
        if grid[i][j] == '#' and grid[i+1][j] != '#':
            grid[i+1][j] = grid[i][j]
            grid[i][j] = '.'

def reduce(grid,nc,nr):
    for k in range(nr*nc):
        move_left(grid,nc,nr)
        move_down(grid,nc,nr)



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

gridd = draw_grid(5, 5, 5,'#')
print("Before Rearrangement")
print_grid(gridd)
print(clustering_distance(gridd))
reduce(gridd,5,5)
print('\n',end= '')
print("After Rearrangement")
print_grid(gridd)
print(clustering_distance(gridd))
print('\n',end= '')
print("After Periodizing")
S = gridd + ReflectionX(gridd)
AggregateY(ReflectionY(S),S)




#The gist of the code is based off cluster analysis. The type of clustering used to measure persistence is hierarchical clustering. We assume that connectivity brings about persistence although the literature is pretty complex on that matter (sometimes the opposite is true; habitat fragmentation brings about species persistences). Hierarchical clustering is different from other clustering models in the sense that it capitalizes upon connectivity as a criterion for grouping objecs (in our case; habitat) together.

#the literature suggests that habitat fragmentation is detrimental to species persistence (but not biodiversity) in the case of single-species models which is the case here. This is numerically clear in the value of the clustering distance = f(connectivity,n) a decreasing function with respect to both variables (with respect to n thanks to single-species model)
