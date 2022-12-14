n = int(input("n = "))
sum1 = sum2 = sum3 = 0
a = list(map(int, input().split()))
b = []
for i in range(n):
    if a[i] % 3 == 0:
        sum1 += 1
    if a[i] > 0:
        sum2 += a[i]
        sum3 += 1
b.append(sum1)
for i in range(n):
    b.append(a[i])
b.append(sum2 // sum3)
print(b)
