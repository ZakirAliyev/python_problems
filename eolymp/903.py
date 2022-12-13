n = int(input())

if n // 100 == n % 10:
    print("=")
elif n // 100 > n % 10:
    print(n // 100)
else:
    print(n % 10)
