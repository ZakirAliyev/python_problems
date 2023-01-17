n = int(input("n = "))
max = 0
while n > 0:
    if n % 10 > max:
        max = n % 10
    n //= 10
print("max = ", max)
