import numpy as np

'''arr1=np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))

print(arr1.shape)'''


arr2=np.array([1,2,3,4,5])
print(arr2.reshape(1,5))

arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2)
print(arr2.shape)

np.arange(0,10,2).reshape(5,1)
print(np.ones((3,4)))

##identity matrix
print(np.eye(3))


arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)