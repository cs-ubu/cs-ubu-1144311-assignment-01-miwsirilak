def readm(fname='A.csv'):
    f = open(fname, 'r') #w, b
    A = []
    for line in f.readlines():
        A.append( [ float(x) for x in line.strip().split(',') ] )
    f.close()
    return A
# 1.read matrix A from 'A.csv'
A = readm('A.csv')

# 2.read matrix b from 'b.csv'
b = readm('b.csv')

# 3.find th result of C = A x b
def matmul(A, b):
    m, n = len(A), len(b[0])
    J = len(A[0]) #A ~ mxJ # b-Jxn
    if len(A[0]) == len(b):
    C = [ [0]*n for i in range(m) ]
    for r in range(m):
        for c in range(n):
            C[r][c] = sum([ A[0][j]*b[j][0] for j in range(J) ])
    return C
return [] #ไม่สามารถคูณได้

# 4.print C
C = matmul(A, b)
print('-----')
for row in C:
    print(row)
print('-----')
# import numpy as np
# D = np.dot(np.array)(A), 