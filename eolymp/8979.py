a = input()
sum = 0
for i in a:
    if i == 'a':
        sum += 1
if sum > 0:
    for i in range(sum):
        print('a', end="")
else:
    print(-1)
