#accessing/changing specific elements, rows, columns etc
import numpy as np
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
print(a.shape)
#get [row, col]
print(a[1,4])

#get specific row
print(a[0, :])

#get specific column
print(a[:, 2])

#more accessors [startindex:endindex:stepsize]
#               [inclusive:exclusive]

print(a[0, 1:6:2])

#changing something
a[1,4] = 20
print(a)

#replace column
a[:, 2] = 5
print(a)

a[:, 2] = [1,2]
print(a)