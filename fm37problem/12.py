n = int(input())

a = list(map(int, input().split()))
i = 0
b = []
flag = True

for i in range(len(a)):
    if a[i] > 0:
        b.append(a[i])
    else:
        break

for i in range(len(b) - 1):
    if b[i] >= b[i + 1]:
        flag = False
        print("False")
        break
if flag:
    print("True")
