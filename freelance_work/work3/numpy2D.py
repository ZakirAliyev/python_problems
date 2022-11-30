"""
Write a NumPy program to create a 3x3 matrix with
 values ranging from 2 to 10.

Expected Output:
[[ 2 3 4]
[ 5 6 7]
[ 8 9 10]]
---------------------------------------------------
2 ilə 10 arasında dəyişən 3x3 matris yaratmaq üçün
NumPy proqramı yazın.

Gözlənilən Nəticə:
[[ 2 3 4]
[ 5 6 7]
[ 8 9 10]]
"""

import numpy as np

x = np.arange(2, 11).reshape(3, 3)
print(x)
