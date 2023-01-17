n = int(input("n = "))
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print("sum = ", sum)
