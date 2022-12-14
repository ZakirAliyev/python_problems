n = int(input())
sum2 = sum1 = 0
a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] > 0:
        sum2 += a[i]
    sum1 += a[i]
print(sum1, sum2)
