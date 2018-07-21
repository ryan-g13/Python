# Character Picture Grid

# Say you have a list of lists where each value in the inner lists is a one-character string, like this:

grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

# You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

# Copy the previous grid value, and write code that uses it to print the image.

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....


# Lesson learned do no try to duplicate a 2-d array unless necesasry.
for i in range(6):
    for j in range(9):
        print(grid[j][i], end='')
    print('\n')