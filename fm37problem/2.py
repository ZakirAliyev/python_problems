n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if a[j] > a[i]:
            a[i], a[j] = a[j], a[i]
print(a)
