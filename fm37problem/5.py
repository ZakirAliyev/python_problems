n = int(input())
a = list(map(int, input().split()))

for i in range(n // 2, n):
    print(a[i], end=" ")
for i in range(n // 2):
    print(a[i], end=" ")
