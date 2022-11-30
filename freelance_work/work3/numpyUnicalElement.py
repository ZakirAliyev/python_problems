"""
Write a NumPy program to find unique rows in a NumPy array.
--------------------------------------------------------------
NumPy massivində unikal sətirləri tapmaq üçün NumPy proqramı yazın.
"""

import numpy as np

x = np.array([[20, 20, 20, 0],
              [0, 20, 20, 20],
              [0, 20, 20, 20],
              [20, 20, 20, 0],
              [10, 20, 20, 20]])
print("Original array:")
print(x)
y = np.ascontiguousarray(x).view(np.dtype((np.void, x.dtype.itemsize * x.shape[1])))
_, idx = np.unique(y, return_index=True)

unique_result = x[idx]
print("Unique rows of the above array:")
print(unique_result)
