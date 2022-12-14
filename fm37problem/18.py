n = int(input("n = "))

a = list(map(int, input().split()))

b = int(input("b = "))
c = int(input("c = "))

d = []
for i in range(n):
    if a[i] < b or a[i] > c:
        d.append(a[i])
print(d)
