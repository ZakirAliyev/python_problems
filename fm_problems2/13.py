"""
13. Tərəfləri x, y, z olan üçbucaq verilmişdir.
Üçbucağın mümkünlük şərtini yoxlayın. Əgər üçbucaq
mövcudursa üçbucağın düzbucaqlı olub olmadığını
yoxlayın ( Üçbucağın mümkünlük şərti :
x+y > z > x-y hər 3 tərəf üçün yoxlanılmalıdır )
"""

a = int(input())
b = int(input())
c = int(input())
if a + b <= c or a + c <= b or b + c <= a:
    print("This triangle not exist.")
else:
    if c ** 2 == a ** 2 + b ** 2 or a ** 2 == c ** 2 + b ** 2 or b ** 2 == a ** 2 + c ** 2:
        print("This triangle rigth triangle.")
