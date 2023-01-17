import math

a, b, c = list(map(float, input("a, b, c = ").split()))
d = b ** 2 - 4 * a * c
if d < 0:
    print("The equation has no roots!")
else:
    x1 = -b + math.sqrt(d) / 2 * a
    x2 = -b - math.sqrt(d) / 2 * a
    if d == 0:
        print("x = ", x1)
    else:
        print("x1 = {}\nx2 = {}".format(x1, x2))
