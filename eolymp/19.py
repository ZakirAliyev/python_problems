sum = 0
a = input()
b = a[::-1]
for i in range(0,len(a)):
    if a[i]==b[i]:
        sum+=1
if len(a)%2==0:
    print(sum // 2)
else:
    print(sum // 2 + 1)