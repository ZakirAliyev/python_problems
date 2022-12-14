n = int(input())
a = list(map(int, input().split()))
max1 = a[0]
for i in range(n):
    if max1 < a[i]:
        max1 = a[i]
print(max1)
