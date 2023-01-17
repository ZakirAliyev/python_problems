n = int(input("n = "))
sum = 0
while n > 0:
    sum += 1
    n //= 10
if sum == 0:
    print("sum = ", 1)
else:
    print("sum = ", sum)
