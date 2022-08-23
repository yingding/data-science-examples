# Python code to demonstrate the working of array(), append(), insert()
# Reference:
# https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/

# array from the array module, all data type in the array must be the same time
# while the list can hold different data type.
import array

# initializing array with array values
# initializes arry with signed integers
arr = array.array('i', [1,2,3])

arr.append(4)

