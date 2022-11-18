n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if c == 0:
    print(a, b, sep="")
else:
    print(c, a, b, sep="")
