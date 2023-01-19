a = input()
sum = 0
m = len(a)
for i in a:
    if i == 'a':
        print(sum,end=" ")
    else:
        m -= 1
    sum += 1
if m == 0:
    print(-1)