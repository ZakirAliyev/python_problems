t = int(input())
for k in range(t):
    n = int(input())
    str = input()
    a = ""
    b = ""
    i = 1
    max = 0
    for x in range(n - 1):
        for y in range(i):
            a += str[y]
        for u in range(i, n):
            b += str[u]
        if len(set(a)) + len(set(b)) > max:
            max = len(set(a)) + len(set(b))
        i += 1
        a = ""
        b = ""
    print(max)
