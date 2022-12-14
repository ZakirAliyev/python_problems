n = int(input("n = "))

a = list(map(int, input().split()))

k = int(input("k = "))
m = int(input("m = "))

for i in range(k - 1, k + m - 1):
    a.append(a[i])
print(a)
