"""
Some mathematical functions and their meanings
"""

import math

n = int(input("n = "))

print(math.ceil(n))        # Returns the smallest integer greater than or equal to x.
print(math.fabs(n))        # Returns the absolute value of x
print(math.factorial(n))   # Returns the factorial of x
print(math.floor(n))       # Returns the largest integer less than or equal to x
print(math.frexp(n))       # Returns the mantissa and exponent of x as the pair (m, e)
print(math.isfinite(n))    # Returns True if x is neither an infinity nor a NaN (Not a Number)
print(math.isinf(n))       # Returns True if x is a positive or negative infinity
print(math.isnan(n))       # Returns True if x is a NaN
print(math.modf(n))        # Returns the fractional and integer parts of x
print(math.trunc(n))       # Returns the truncated integer value of x
print(math.exp(n))         # Returns e**x
print(math.log1p(n))       # Returns the natural logarithm of 1.1  Введение в курс+x
print(math.log2(n))        # Returns the base-2 logarithm of x
print(math.log10(n))       # Returns the base-10 logarithm of x
print(math.sqrt(n))        # Returns the square root of x
print(math.cos(n))         # Returns the cosine of x
print(math.sin(n))         # Returns the sine of x
print(math.tan(n))         # Returns the tangent of x
print(math.degrees(n))     # Converts angle x from radians to degrees
print(math.radians(n))     # Converts angle x from degrees to radians