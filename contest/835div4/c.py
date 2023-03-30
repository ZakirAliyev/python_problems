t = int(input())

for essa in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    posortowane = sorted(s)
    for i in range(n):
        if s[i] == posortowane[-1]:
            print(s[i] - posortowane[-2], end=" ")
        else:
            print(s[i] - posortowane[-1], end=" ")
    print()
