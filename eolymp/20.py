n = int(input())
sum = 0
h = n
while h != 0:
    while n != 0:
        m = n % 10
        h -= m
        n //= 10
    sum += 1
    n = h
print(sum)
