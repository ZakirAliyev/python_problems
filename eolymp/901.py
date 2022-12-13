a = input()
sum = 0
for i in range(len(a)):
    if a[i] == '-' or a[i] == '+' or a[i] == '*':
        sum += 1
if a[0] == '-' or a[0] == '+' or a[0] == '*':
    print(sum - 1)
else:
    print(sum)
