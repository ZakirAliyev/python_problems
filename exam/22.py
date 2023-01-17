n = int(input("n = "))
even = odd = 0
while n > 0:
    if n % 10 % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print("even = {}\nodd = {}".format(even, odd))
