n = int(input())
lst = list(map(int, input().split()))
cem = 0

for i in range(n - 1, -1, -1):
    if i == 1 or i == 0:
        break
    cem += min(lst[i - 1], lst[i - 2])
    if min(lst[i - 1], lst[i - 2]) == lst[i - 1]:
        i -= 1
    else:
        i -= 2

print(cem + lst[n - 1])
