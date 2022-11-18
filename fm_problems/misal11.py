a = int(input())
c = 0
while a != 0:
    b = a % 10
    c = c * 10 + b
    a //= 10
print(str(c))
