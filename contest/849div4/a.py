n = int(input())
str = "codeforces"
for i in range(n):
    flag = True
    s = input()
    for i in str:
        if i == s:
            print("YES")
            flag = False
            break
    if flag:
        print("NO")
