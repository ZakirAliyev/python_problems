k = int(input())
for i in range(k):
    n = int(input())
    s = input()
    s = s.lower()
    str1 = ""
    for j in s:
        if j not in str1:
            str1 += j
    if str1 == "meow":
        print("YES")
    else:
        print("NO")



