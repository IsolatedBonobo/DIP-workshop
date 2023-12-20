# numpy is just like list 

# address in numpy are continous 

import numpy as np 
# array intialisaation 

arr = np.array([[1,23,4,5,6 ] , [2,9,8,7,6]])

print(arr)



# functions in numpy array
# np.size(array name) or arr.size()
# np.shape(array name) or arr.shape() returns the dimension of the array
# np.arange(start, end, stepping index)
# np.ones(shape) will create a array including ones in the matrix of shape
# np.zeroes same as ones but zeroes in place of ones
# np.eye(either row or coloumn number) will create an identity matrix of given size 
# np.full(shape, number) will return a matrix of given number in given shape 

nrrr = np.eye(3)
print(nrrr)


# np.ndim(arr) will return the dimension of an array 
# np.random.random(shape) this will make an array of shape size consist of all float no between zero to one 
# array.reshape(shape) wiil reshape the matrix is as transpose 

srr = arr.reshape((5,2))
print("srr",srr)



# numpy array slicing 
# if step is +ve then we will move LTR
# if step is -ve then we will move RTL
# arr[1:2, 2:4] this will select 1st row to 2 row(excluding) and 2nd coloumn to 4 coloumn(excluding)
# arr[:, 2 : 4] this will take whole row with given number of coloumns 

# np.matmul(matrix_a, matrix_b)

ans = np.ones((5,5))
print(ans)

z = np.zeroes((3,3))
z[1,1] = 9
print(z)

ans[1:4, 1:4] = z 
print(ans)


# imread function 
