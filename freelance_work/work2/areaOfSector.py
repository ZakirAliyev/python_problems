"""
Write a Python program to calculate the area of the sector.

Test Data:
Radius of a circle : 4
Angle measure : 45

Expected Output:
Sector Area: 6.285714285714286
---------------------------------------------------------------------------
Sektorun sahəsini hesablamaq üçün Python proqramı yazın.

Test Məlumatı:
Dairənin radiusu : 4
Bucaq ölçüsü : 45

Gözlənilən Nəticə:
Sektor Sahəsi: 6.285714285714286
"""


def sectorarea():
    pi = 22 / 7
    radius = float(input('Radius of Circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    sur_area = (pi * radius ** 2) * (angle / 360)
    print("Sector Area: ", sur_area)


sectorarea()
