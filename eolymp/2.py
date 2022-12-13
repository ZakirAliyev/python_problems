n = int(input())
sum = 0
if n == 0:
    print(1)
else:
    while n != 0:
        sum += 1
        n //= 10
    print(sum)
