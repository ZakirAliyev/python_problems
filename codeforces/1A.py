n, m, a = map(int, input().split())
sum = sum1 = 0
if n % a == 0:
    sum += (n // a)
else:
    sum += (n // a + 1)
if m % a == 0:
    sum1 += (m // a)
else:
    sum1 += (m // a + 1)
print(sum * sum1)
