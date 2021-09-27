# Program to add two matrices using nested loop

A = [[1, 2, 3],
     [7, 8, 9],
     [3, 21, 11]]

B = [[9, 8, 7],
     [3, 2, 1],
     [33, 21, 11]]

C = [[0, 0, 0], [0, 0, 0], [0,0, 0]]

# iterate through rows
for i in range(len(A)):
    # iterate through columns
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]

for r in C:
    print(r)
