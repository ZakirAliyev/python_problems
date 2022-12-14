n = int(input("n = "))
sum1 = 0
a = list(map(int, input().split()))

t = int(input("t = "))

for i in range(n):
    if a[i] > 0:
        sum1 += 1
for i in range(n):
    if a[i] > 0:
        a[i] += t // sum1
print(a)
