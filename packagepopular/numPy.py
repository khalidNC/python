'''
NumPy, short for Numerical Python, is a powerful library in Python for numerical and mathematical operations. 
It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical 
functions to operate on these elements. NumPy is the foundation for many other scientific computing libraries 
in Python. Here's an overview of some key aspects of NumPy, along with example codes and explanations:

1. Creating NumPy Arrays:
NumPy arrays are the fundamental data structure provided by the library. They are similar to Python lists but 
more efficient for numerical computations.

Example:
'''

import numpy as np

# Create a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(arr_1d)
'''
OutPut: 
        [1 2 3 4 5]
'''
# print(arr_2d)
'''
OutPut:
        [[1 2 3]
         [4 5 6]
         [7 8 9]]
'''

'''
2. Array Operations:
NumPy provides various operations for manipulating arrays, such as element-wise operations, array addition, 
subtraction, multiplication, etc.

Example:
'''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
result_addition = arr1 + arr2
# print(result_addition)
'''
OutPut:
        [5 7 9]
'''

# Element-wise multiplication
result_multiplication = arr1 * arr2
# print(result_multiplication)
'''
OutPut:
        [ 4 10 18]
'''

'''
3. Universal Functions (ufunc):
NumPy provides a collection of universal functions that operate element-wise on arrays. These functions are optimized 
and can significantly improve performance.

Example:
'''

arr = np.array([1, 2, 3, 4, 5])

# Square root of each element
result_sqrt = np.sqrt(arr)

# Exponential of each element
result_exp = np.exp(arr)


'''
4. Indexing and Slicing:
NumPy allows for advanced indexing and slicing of arrays, enabling efficient access to subarrays or individual 
elements.

Example:
'''

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access element at row 1, column 2
element = arr[1, 2]

# Slice rows 0 to 1, columns 1 to 2
subarray = arr[0:2, 1:3]


'''
5. Array Shape and Reshaping:
You can check and modify the shape of an array using NumPy functions. Reshaping allows you to change the dimensions 
of an array.

Example:
'''
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Get the shape of the array
shape = arr.shape  # Returns (2, 3)

# Reshape the array to a 1D array
reshaped_arr = arr.reshape(-1)
# print(reshaped_arr)

# OutPut: [1 2 3 4 5 6]


'''
6. Array Aggregation:
NumPy provides functions for aggregating data, such as computing the mean, sum, maximum, and minimum of an array.

Example:
'''
arr = np.array([1, 2, 3, 4, 5])

# Compute the mean
mean_value = np.mean(arr)
# print(mean_value)
# OutPut: 3.0

# Compute the sum
sum_value = np.sum(arr)


'''
7. Linear Algebra Operations:
NumPy provides a module for linear algebra operations, including matrix multiplication, eigenvalues, 
and solving linear equations.

Example:
'''
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result_matrix = np.dot(matrix_A, matrix_B)
# print(result_matrix)

'''
OutPut:
        [[19 22]
         [43 50]]
'''

'''
Linear algebra is often used to solve systems of linear equations. Consider a system of equations:
2x + y = 5
3x - 2y = -8
'''
import numpy as np

# Coefficient matrix
coeff_matrix = np.array([[2, 1], [3, -2]])

# Right-hand side vector
rhs_vector = np.array([5, -8])

# Solve the system of linear equations
solution = np.linalg.solve(coeff_matrix, rhs_vector)

# print("Solution:")
# print(solution)

# Another example let's say we have a dimention in inches and we need to convert it to cm
dimention_in_inches = np.array([4, 8, 13])
# 1 inche = 2.54 cm
dimention_in_cm = dimention_in_inches * 2.54

print(dimention_in_cm)
# OutPut: [10.16 20.32 33.02]


# Now let's see if we wnat to do this in pure python without numpy the code will be longer as below:

# Let's say we have a dimention in a reguler list 
dimnetion_inch = [4, 8, 13]

# To transfor this array to a different array we need to use list comprehension
# The syntax is: [item for item in list] here our list is dimention_inche amd let's call the item as i
# and it returns dimention_in_centimeter
dimention_in_centimeter = [i * 2.54 for i in dimnetion_inch]
print(dimention_in_centimeter)
