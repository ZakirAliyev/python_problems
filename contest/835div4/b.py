t = int(input())
for i in range(t):
    max = 96
    n = int(input())
    str = input()
    for j in str:
        if ord(j) > max:
            max = ord(j)
    print(max - 96)
