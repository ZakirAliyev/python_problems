n = int(input("n = "))

a = list(map(int, input().split()))

for i in range(2, n):
    if a[i] == 0:
        a[i] = a[i - 1] + a[i - 2]
print(a)
