n = int(input("n = "))

a = list(map(int, input().split()))
b = []

for i in range(n):
    if a[i] != 0:
        b.append(a[i])
print(b)
