#reorganizing arrays
import numpy as np

#can reshape arrays as long as new shape has same number of values
before = np.array([[1,2,3,4], [5,6,7,8]])
print(before)
print(before.shape)

after = before.reshape((8,1))
print(after)
print(after.reshape((2,2,2)))

#vertically stack vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v2,v2]))

#horizontal stacks
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack([h1, h2]))