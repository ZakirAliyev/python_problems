tuple = tuple(map(int, input().split()))
sum = 0
for i in tuple:
    if i < 7:
        sum += 1
print("sum = ", sum)