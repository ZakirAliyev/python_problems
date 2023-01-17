a, b, c, = list(map(int, input("a, b, c = ").split()))
if a + b > c and a + c > b and c + b > a:
    print("Yes")
else:
    print("No")
