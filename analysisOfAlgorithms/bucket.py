import math


def find_water(bucket1_capacity, bucket2_capacity, target_capacity):
    water1 = 0
    water2 = 0
    print(water1, water2)
    water1 = bucket1_capacity
    print(water1, water2)
    while water1 + water2 != target_capacity:
        if water2 == bucket2_capacity:
            water2 = 0
        elif water1 == 0:
            water1 = bucket1_capacity
        else:
            transfer = min(water1, bucket2_capacity - water2)
            water1 -= transfer
            water2 += transfer
        print(water1, water2)


n, m, k = map(int, input("n, m, k = ").split())

if k == n or k == m:
    print("YES")
    print(0, k, end=" ")
elif n + m == k:
    print("YES")
    print(n, m, end=" ")
elif k <= n + m and k % math.gcd(n, m) == 0:
    print("YES")
    print(find_water(n, m, k))
else:
    print("NO")
