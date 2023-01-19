a = input()
b = a[::-1]
sum = 0
for i in a:
    if i == ' ':
        sum += 1
if sum > 0:
    sum = 0
    for i in a:
        if i == ' ':
            print(sum, end=" ")
            break
        sum += 1
    sum = 0
    for i in b:
        if i == ' ':
            print(len(a) - sum - 1)
            break
        sum += 1
else:
    print(-1)
