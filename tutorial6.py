#miscellaneous
import numpy as np
#load data from file

filedata = np.genfromtxt('data.txt', delimiter=",")
print(filedata)
print(filedata.astype("int32"))

## boolean masking and advanced indexing
print(filedata > 50)

#get all values that meet condition
print(filedata[filedata > 50])

#index multiple elements at once
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

#if you look downwards on columns are any of the values greater than 50
print(np.any(filedata > 50, axis=0))
print(np.all(filedata > 50, axis=0))

#axis=1 looks per row
print(np.any(filedata > 50, axis=1))
print(np.all(filedata > 50, axis=1))

#multiple conditions and boolean operators
print(~((filedata > 50) & (filedata < 100)))