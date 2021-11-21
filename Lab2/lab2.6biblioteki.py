#pip install numpy

import numpy as np

A=np.array([[1,2],[5,6]])
B=np.array([3,4])

N = 10
A=np.random.randn(N,N)
B=np.array(range(1,N+1))

print('Macierz A:')
print(A)
print('Wektor B:')
print(B)

w=np.linalg.det(A)
print('Wyznacznik z macierzy A = ',w)

x=np.linalg.solve(A,B)
print('Rozwiazanie:')
print(x)

print('Iloczyn A*x')
print(np.dot(A,x))

