import numpy as np

# Rows of the matrix
r1 = [3,-2,5,6,11]
r2 = [2,3,-4,0,8]
r3 = [5,6,-3,2,1]
r4 = [-2,5,7,-1,-2]
matrix = [r1,r2,r3,r4]

print(np.matrix(matrix))
print()

# Helper Functions
# Adds row2 to row1
def addRows(row1,row2) :
  for i in range(0,len(row1)) :
    row1[i] = row1[i] + row2[i]
  print(np.matrix(matrix))
  print()

# Scales row by scalar value
def scaleRow(row,scalar) :
  scaledRow=[None]*len(row)
  for i in range(0,len(row)) :
    scaledRow[i] = row[i] * scalar
  return scaledRow

# Swaps row1 and row2
def swapRows(row1,row2) :
  for i in range(0,len(row1)) :
    row1[i],row2[i] = row2[i],row1[i]
  print(np.matrix(matrix))
  print()
  
## Gauss Elimination Test
# print("Row 1 Operations")
# addRows(r1,r4)
# addRows(r2,scaleRow(r1,-2))
# addRows(r3,scaleRow(r1,-5))
# addRows(r4,scaleRow(r1,2))

# print("Row 2 Operations")

# addRows(r1,r2)
# addRows(r3,scaleRow(r2,-3))
# swapRows(r4,scaleRow(r4,3))
# addRows(r4,scaleRow(r2,11))

# print("Row 3 Operations")

# swapRows(r1,scaleRow(r1,21))
# swapRows(r2,scaleRow(r2,21))
# swapRows(r4,scaleRow(r4,21))
# addRows(r1,scaleRow(r3,16))
# addRows(r2,scaleRow(r3,28))
# addRows(r4,scaleRow(r3,215))

# print("Row 4 Operations")

# swapRows(r1,scaleRow(r1,34))
# swapRows(r2,scaleRow(r2,-17))
# swapRows(r3,scaleRow(r3,34))
# addRows(r1,r4)
# addRows(r2,r4)
# addRows(r3,r4)

