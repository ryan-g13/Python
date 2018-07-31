#! python3

# input of a list of lists of strings and returns a organized tale that is right justified. 

tableData = [['apples', 'oranges', 'cherries', 'banana', 'watermelon'],
             ['Alice', 'Bob', 'Carol', 'David', 'Jimmy'],
             ['dogs', 'cats', 'moose', 'goose', 'cow']]

def printTable(data): 
  columnWidth = []
  maxVal = 0
  # Finding the max column width necessary for printing out right justified.
  for k in data:
    maxVal = 0
    for j in k: 
       if len(j) > maxVal :
         maxVal = len(j)
    columnWidth.append(maxVal)
  
  colNum = len(data)
  rowNum = len(data[0])
  fullCol = ''
  # Printing the table values out right justified with a table header full width of the characters in the table
  print('Table Values'.center(columnWidth[0] + columnWidth[1] + columnWidth[2] + 2, '-'))
  for r in range(rowNum):
    fullCol = '' 
    for c in range(colNum):
      fullCol += data[c][r].rjust(columnWidth[c]) + ' '
    print(fullCol.rstrip())

printTable(tableData)