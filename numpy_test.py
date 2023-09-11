# now let's test working with numpy

# first we need to import the numpy library 
import numpy as np

# we can define a vector array called v1 by using numpy library
v1 = np.array([1, 2, 3, 4, 5, 6])
print(v1)
# this way you can see that the v is saved as an array instead of a list 

# This is for defining another vector array
v2 = np.array([7, 8, 9, 10, 11, -12])
print(v2)

# we can do several vector operations
print(v1 + v2)
# here the vectors should be of the same length

# we can also do dot product for these vectors
print (v1 * v2)

# we can use shape to check the tuple and the number of corresponding elements in each index
print(v1.shape) # it shows that v1 is 6 times nothing matrix 

# if we want to make it a 6 by 1 vector:
v1 = np.array([[1], [2], [3], [4], [5], [6]])
print(v1.shape)

# we do the same with v2
v2 = np.array([[7], [8], [9], [10], [11], [12]])
print(v2.shape)

# in order to do matrix multiplication, we should multiply one by the transpose of the other 
# we use the function matmul to do matrix multiplication, and the "transpose" is for transposing the matrix
print(np.matmul(v1,v2.T))
print("or")
print(np.matmul(v1,np.transpose(v2))) # this matrix is 6 by 6
print(v2.T.shape) # see that it is a 1 by 6 matrix 

# @ also means matrix multiplication 
print(v1.T @ v2) # which is a 1 by 1 vector or just a number

# if we want to write a for example 2 by 6 matrix:

x = np.array([[[1], [2], [3], [4], [5], [6]],[[7], [8], [9], [10], [11], [12]]])
print(x.shape)