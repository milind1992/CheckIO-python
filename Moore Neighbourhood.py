'''
Created on 25-Jun-2016
​
@author: milind
'''
def count_neighbours(grid, row, col):
    # Get the number of rows and columns
    cmax=len(grid[0])
    rmax=len(grid)
    
    # To get the surrounding 8 co-ordinates , we use the check array to get the values.
    check =[-1,0,1]
    # Get all the neighborhood values
    NeighborhoodValues=[grid[x+row][y+col] for x in check if x+row >=0 and x+row<rmax for y in check if y+col >= 0 and y+col<cmax]
    
    # Check if the center value is 1 or not
    if grid[row][col]==1:
        # if it is then subtract 1 from the final count
        return NeighborhoodValues.count(1)-1
    else: 
        # If not send the final count 
        return NeighborhoodValues.count(1)
​
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"