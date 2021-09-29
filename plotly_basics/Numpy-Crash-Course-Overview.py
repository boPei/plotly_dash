####################################
# Numpy Crash Course ###############
####################################

import numpy as np
np.random.seed(101)

my_list=[0,1,2,3,4]
arr=np.array(my_list)
print(arr)

# arange integers, takes in start, stop and step size
arr=np.arange(0,10)
print(arr)

arr=np.arange(0,10,2)
print(arr)

# create an array of zeros
arr=np.zeros((5,5))
print(arr)

# create an array of ones
arr=np.ones((2,4))
print(arr)

# create an array of random integers(uniform distribution between limits)
arr=np.random.randint(0,10)
print(arr)

# create a 2d matrix random ints
arr=np.random.randint(0,10,(3,3))
print(arr)

# create linearly spaced array
arr=np.linspace(0,10,6)
print(arr)

arr=np.linspace(0,10,101)
print(arr)


arr=np.random.randint(0,100,10)
print(arr)

# reshape array
arr=arr.reshape(2,5)
print(arr)

# Indexing elements in a matrix
mat=np.arange(0,100).reshape(10,10)
print(mat)
arr_ele=mat[5,2]
print(arr_ele)

arr_col=mat[:,2]
print(arr_col)

arr_row=mat[2,:]
print(arr_row)

# masking allows you to use the conditional elements to grab the elements
arr_condition=mat>50
print(arr_condition)

arr_mat=mat[arr_condition]
print(arr_mat)