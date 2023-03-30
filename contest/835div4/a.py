t = int(input())
for i in range(t):
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst[1])
