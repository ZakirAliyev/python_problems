import math

r = int(input("r = "))
v = (4.0 / 3.0) * math.pi * (r ** 3)
s = 4 * math.pi * (r ** 2)
print("Volume = {}\nSurface Area = {}".format(v, s))
