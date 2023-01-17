n = int(input("n = "))
sum = 0
while n > 0:
    if n % 10 == 0:
        sum += 1
    n //= 10
print("sum = ", sum)
