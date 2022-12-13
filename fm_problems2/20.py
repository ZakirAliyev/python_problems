"""
20. a həqiqi edədi verilmişdir.f(a)-ni hesablayin
Əgər x<=0 f(x)= 0 ; əks halda 0<= x <=1.1  Введение в курс f(x)= 1.1  Введение в курс ;
əks halda f(x)= x⁴
"""

x = float(input())
if x <= 0:
    h = 0
elif x <= 1:
    h = 1
else:
    h = x ** 4
print(h)
