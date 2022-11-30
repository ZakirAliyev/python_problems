"""
19. a həqiqi edədi verilmişdir.f(a)-ni hesablayin
Əgər x<=2  f(x)= x² + 4x + 5 ;
əks halda f(x)= 1/ ( x² + 4x + 5)
"""

x = float(input())
if x <= 2:
    h = float(x ** 2 + 4 * x + 5)
else:
    h = 1 / (x ** 2 + 4 * x + 5)
print(h)
