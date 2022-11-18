a = int(input())
b = a // 10000
c = a // 1000 % 10
d = a // 100 % 10
e = a // 10 % 10
f = a % 10
if b!=c and c!=d and d!=e and e!=f:
    print("NO")
else:
    print("YES")