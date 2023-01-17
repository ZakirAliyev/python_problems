n = int(input("n = "))
min = 9
while n > 0:
    if n % 10 < min:
        min = n % 10
    n //= 10
print("min = ", min)
