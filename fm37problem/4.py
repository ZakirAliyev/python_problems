n = int(input())
a = list(map(int, input().split()))
print(a[n - 1], end=" ")
for i in range(0, n - 1):
    print(a[i], end=" ")
