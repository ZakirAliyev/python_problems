t = int(input())
for j in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    a = 2
    flag = True
    for i in range(len(lst) - 1):
        if a == 1 and lst[i] > lst[i + 1]:
            flag = False
            break
        if lst[i] < lst[i + 1]:
            a = 1
        elif lst[i] > lst[i + 1]:
            a = 2
    if flag:
        print("YES")
    else:
        print("NO")
