t = int(input())
for k in range(t):
    i = j = 0
    flag = True
    n = int(input())
    str = input()
    for a in str:
        if a == 'U':
            i += 1
        elif a == 'R':
            j += 1
        elif a == 'D':
            i -= 1
        elif a == 'L':
            j -= 1
        if i == 1 and j == 1:
            print("YES")
            flag = False
            break
    if flag:
        print("NO")
