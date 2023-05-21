n = int(input())
lst = list(map(int, input().split()))
lst2 = []
for i in lst:
    k = 0
    for j in lst:
        if i == j:
            k += 1
    if k < 2:
        lst2.append(i)
for i in lst2:
    print(i, end=" ")
