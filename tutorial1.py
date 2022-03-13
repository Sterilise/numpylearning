import numpy as np

#creating 1 dimensional array
a = np.array([1,2,3])
print(a)

#two dimensional array
b = np.array([[1.0,2.0,3.0], [1.0,2.0,4.0]])
print(b)

#get dimesnions
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get type
print(a.dtype)

aa = np.array([1,2,3], dtype="int16")
print(aa.dtype)

#get size (memory)
#bytes per item
print(a.itemsize)
print(aa.itemsize)
#total number of elements
print(a.size)
print(aa.size)
#total number of bytes
print(a.nbytes)
print(b.nbytes)
print(aa.nbytes)