n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if b == 0:
    print(c, a, sep="")
else:
    print(b, c, a, sep="")
