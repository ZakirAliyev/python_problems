n = int(input())
flag = "Number is prime"
for i in range(2, n):
    if n % i == 0:
        flag = "Number is complex"
        break
print(flag)
