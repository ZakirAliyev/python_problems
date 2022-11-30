"""
Write a NumPy program to swap rows and
columns of a given array in reverse order.
----------------------------------------------------
Verilmiş massivin sətir və sütunlarını tərs
qaydada dəyişdirmək üçün NumPy proqramını yazın.
"""

import numpy as np

nums = np.array([[[1, 2, 3, 4],
                  [0, 1, 3, 4],
                  [90, 91, 93, 94],
                  [5, 0, 3, 2]]])
print("Original array:")
print(nums)
print("\nSwap rows and columns of the said array in reverse order:")
new_nums = print(nums[::-1, ::-1])
print(new_nums)
