"""
17. Verilmiş x və y həqiqi ədədlərinə uyğun olaraq z-i
hesablayın. Əgər x > y, Z=  ✓( x * y ) əks halda Z= ln(x+y)
"""

import math

x = int(input())
y = int(input())
if x > y:
    z = mathh.sqrt(x * y)
else:
    z = mathh.log10(x + y)
print(z)
