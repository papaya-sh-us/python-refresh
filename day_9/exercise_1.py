import numpy as np

a = np.array([1, 2, 3])                 
b = np.array([[1, 2, 3], [4, 5, 6]])  

print(np.zeros(5))          
print(np.ones((2, 3)))      
print(np.arange(0, 10, 2))  
print(np.linspace(0.0, 1.0, 5)) 

print(a.shape)              
print(a.ndim)               
print(a.dtype) 
print(b.shape)              
print(b.ndim)               
print(b.dtype)              