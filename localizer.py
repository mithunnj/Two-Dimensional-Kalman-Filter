# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == color:
                beliefs[i][j] = beliefs[i][j]*p_hit
            else:
                beliefs[i][j] = beliefs[i][j]*p_miss 
    
    total = 0
    total_list = []
    
    for i in beliefs:
        total = sum(i)
        total_list.append(total)
        
    total_sum = sum(total_list)
    
    for x in range(len(beliefs)):
        for y in range(len(beliefs[0])):
            beliefs[x][y] = beliefs[x][y] / total_sum

    return beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)
