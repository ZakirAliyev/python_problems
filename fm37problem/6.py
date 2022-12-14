n = int(input("n = "))
a = list(map(int, input().split()))
k = int(input("k = "))
p = int(input("p = "))
m = int(input("m = "))

if p < k:
    p, k = k, p

for i in range(k - 1):
    print(a[i], end=" ")
for i in range(p - 1, p + m - 1):
    print(a[i], end=" ")

for i in range(p - 2, p - 1):
    print(a[i], end=" ")

for i in range(k - 1, k + m - 1):
    print(a[i], end=" ")

for i in range(p + m - 1, len(a)):
    print(a[i], end=" ")
