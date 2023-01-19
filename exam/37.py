a, b = list(map(int, input("a, b = ").split()))
while b > 0:
    a, b = b, a % b
    """
    c = a % b
    a = b
    b = c
    """
print(a)
