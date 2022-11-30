"""
16. Verilmiş A, B, C-yə uyğun olaraq bu
şərtləri yoxlayın A < B < C və ya A >= B >= C
"""

a = int(input())
b = int(input())
c = int(input())
mi = min(c, min(a, b))
ma = max(c, max(a, b))
if (min == a and max == c) or (min == c and max == a):
    print("True")
else:
    print("False")
