m = int(input())
a = []
for i in range(m):
    elem = input()
    a.append(elem)

max1 = 0

for i in range(m):
    if len(a[i]) > max1:
        max1 = len(a[i])

for i in range(m):
    d = max1 - len(a[i])
    print(d * "*", end="")
    print(a[i], end="\n")
