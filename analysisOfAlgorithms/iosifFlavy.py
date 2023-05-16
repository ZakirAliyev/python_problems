n, m = map(int, input().split())
a = list(range(1, n + 1))
k = 0
c = 0

while len(a) > 1:
    k += 1
    if k == m:
        a.pop(c)
        k = 0
        c -= 1
        n -= 1
        if n == 0:
            break
    c += 1
    if c == n:
        c = 0

print(a[0])

