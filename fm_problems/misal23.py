a = int(input())
b = 0
while a != 0:
    c = a % 10
    b = b * 10 + c
    a //= 10
print(b)