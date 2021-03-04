import numpy as np

x = np.random.random(size=10)
print("Before slicing, x: ",x)
x = x[:-1]
x1=x[-1]
print("After slicing, x: ",x,"x1:",x1)