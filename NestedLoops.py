# this is for the nested loop section
# nested loops --> loops inside the loops

# we can iterate over the elements of a 2D list using nested loops
# the outer loop iterates over the rows 
# the inner loop iterates over the columns 

# let's go back to the example of the 2D list
grid = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

# Iterate over the elements of the grid using nested loops
for row in grid:
    for column in row:
        print(column)