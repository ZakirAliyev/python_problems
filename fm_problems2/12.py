"""
12. Tili A-ya bərabər olan kub və hündürlüyü H,
oturacağı R-ə bərabər slindir verilib. M litr maye verilib.
Bu maye ilə verilmiş slindri və kubu doldurmaq olarmi?
"""

import math

a = int(input("a = "))
h = int(input("h = "))
r = int(input("r = "))
x = int(input("x = "))

vk = a ** 2
vs = mathh.pi * r ** 2 * h

if x <= vk and x <= vs:
   print("The liquid settles in both the cylinder and the cube.")
elif x <= vk:
   print("The liquid settles only the cube.")
elif x <= vs:
   print("The liquid settles only the cylinder.")
else:
   print("The liquid is neither in the cylinder nor in the cube.")