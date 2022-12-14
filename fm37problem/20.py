n = int(input("n = "))

a = list(map(int, input().split()))
flag = False

for i in range(1, n):
    if a[i] == 0 and a[i - 1] == 0:
        flag = True
        print("True")
        break
if not flag:
    print("False")
