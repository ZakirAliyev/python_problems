t = int(input())
for k in range(t):
    n = int(input())
    str = input()
    i = 1
    j = 0
    lenn = len(str)
    while True:
        if lenn == 0:
            break
        elif str[j] == str[len(str) - i]:
            break
        elif str[j] != str[len(str) - i]:
            i += 1
            j += 1
            lenn -= 2
    print(lenn)
