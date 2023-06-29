import numpy as np
import random


def draw_grid(ng,nk,nr,nc,g,k): #n is n+ in the article
  # Create a grid of all white squares
  grid = [['.' for i in range(nr)] for j in range(nc)]

  # Randomly select n squares to be shaded black (habitat) symbolized as #
  L = [[]]
  for i in range(ng):
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
  def IsEqual(S,a,b):
      equality = False
      for k in range(len(S)):
          equality+= bool([a,b] == S[k])
      return equality

  C = [[]]
  for i in range(nk):
    x = random.randint(0, nr-1)
    y = random.randint(0, nc-1)
    if [x,y] != C[i]:
        if not IsEqual(L,x,y):
            C.append([x,y])
            grid[x][y] = k
    else:
      while [x,y] == C[i] or IsEqual(L,x,y):
        x = random.randint(0, nr-1)
        y = random.randint(0, nc-1)
      C.append([x,y])
      grid[x][y] = k

  return grid

def move_left(grid,nc,nr):
   #Shift all the squares in each row to the left
  for i in range(nr):
    for j in range(1,nc):
        if grid[i][j] == '#' and grid[i][j-1] != '#':
            grid[i][j-1] = grid[i][j]
            grid[i][j] = '.'

def move_right(grid,nc,nr):
   #Shift all the squares in each row to the right
  for i in range(nr):
    for j in range(nc-1):
        if grid[i][j] == '#' and grid[i][j+1] != '#':
            grid[i][j+1] = grid[i][j]
            grid[i][j] = '.'

def move_up(grid,nc,nr):
   #Shift all the squares in each column to the up
  for i in range(1,nr):
    for j in range(nc):
        if grid[i][j] == '#' and grid[i-1][j] != '#':
            grid[i-1][j] = grid[i][j]
            grid[i][j] = '.'


def move_down(grid,nc,nr):
   #Shift all the squares in each column to the down
  for i in range(nr-1):
    for j in range(nc):
        if grid[i][j] == '#' and grid[i+1][j] != '#':
            grid[i+1][j] = grid[i][j]
            grid[i][j] = '.'

def reduce(grid,nc,nr):

    for i in range(nr):
      for j in range(nc):
        if grid[i][j] == '#':
          for k in range(nr):
            move_down(grid,nc,nr)
            move_left(grid,nc,nr)
    for i in range(nr):
      for j in range(nc):
        if grid[i][j] == '@':
          for k in range(nr):
            move_up(grid,nc,nr)
            move_right(grid,nc,nr)




#def competition(grid, p,f, d):
  #  draw_grid(ng,nk,nr,nc,g,k)

#def conversion(grid,p,f,d):
    #draw_grid(ng,nk,nr,nc,g,k)



def print_grid(grid):
  for row in grid:
    for square in row:
      print(square, end=' ')
    print()

gridd = draw_grid(10,5, 15, 15,'#','@')
print_grid(gridd)

reduce(gridd,15,15)
print('\n',end='')

print_grid(gridd)
