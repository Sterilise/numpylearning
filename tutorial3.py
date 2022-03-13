#nitializing different types of arrays
import numpy as np

#All 0s matrix
a = np.zeros(5)
b = np.zeros((2,3))

print(a)
print(b)

#All 1s matrix

c = np.ones((4,2,2), dtype="int32")
print(c)

#Any other number
d = np.full((2,2), 99, dtype="float32")
print(d)

# Any other number (full_like)
e = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
f = np.full_like(e, 4)
print(f)

#random decimal numbers
g = np.random.rand(4,2, 3)
print(g)

#random decimal numbers with existing shape
h = np.random.random_sample(a.shape)
print(h)

#random integer values start, end (exclusive)
i = np.random.randint(0, 7, size=(3,3) )
print(i)

#identity matrix
j = np.identity(5)
print(j)

#repeat an array some times
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
r2 = np.repeat(arr, 3, axis=1)
print(arr)
print(r1)
print(r2)

#initialise custom array

k = np.ones((5,5), dtype="int32")
k[1:-1, 1:-1] = np.zeros((3,3), dtype="int32")
k[2,2] = 9

print(k)

#be careful when copying arrays

l = np.array([1,2,3])
m = l.copy()
print(l)
print(m)
m[0]=100
print(m)
print(l)

