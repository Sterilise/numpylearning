#mathematics
import numpy as np

#elementwise arithmetic
a = np.array([1,2,3,4])
print(a)
print(a + 2)
print(a - 1)
print(a * 2)
print(a / 2)
a *= 2
print(a)

#other array
b = np.array([1,0,1,0])
print((a + b) ** 2)

#elementwise functions
print(np.cos(b))

#Linear algebra

#matrix multiplication
c = np.ones((2,3))
print(c)
d = np.full((3,2), 2)
print(d)

print(np.matmul(c,d))

#determinent of matrix

e = np.identity(3)
print(np.linalg.det(e))

##statistics

stats = np.array([[1,2,3], [4,5,6]])

print(np.min(stats))
print(np.max(stats))
#1 level in
print(np.min(stats, axis=1))
#0 levels in
print(np.min(stats, axis=0))
print(np.sum(stats))
print(np.sum(stats, axis=0))