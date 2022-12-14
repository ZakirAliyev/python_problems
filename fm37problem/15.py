n = int(input())
sum1 = sum2 = 0
a = list(map(int, input().split()))

for i in range(n):
    if a[i] < 0:
        sum1 += 1
    elif a[i] > 0:
        sum2 += 1
if sum1 != sum2:
    b = abs(sum1 - sum2)
else:
    b = 0
for i in range(b):
    if sum1 < sum2:
        a.append(-1)
    else:
        a.append(1)
print(a)
