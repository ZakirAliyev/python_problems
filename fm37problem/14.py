n = int(input())

a = list(map(int, input().split()))

b = []
c = []

for i in range(n):
    if a[i] < 0:
        b.append(a[i])
    elif a[i] > 0:
        c.append(a[i])

print(b, c, sep="\n")
