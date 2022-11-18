a = int(input())
b = a // 10000
c = a // 1000 % 10
e = a // 10 % 10
f = a % 10
if b == f and c == e:
    print("YES")
else:
    print("NO")
