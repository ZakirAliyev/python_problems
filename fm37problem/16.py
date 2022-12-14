n = int(input())
menfi = musbet = 0
a = list(map(int, input().split()))

for i in range(n):
    if a[i] < 0:
        menfi += a[i]
    elif a[i] > 0:
        musbet += a[i]
if menfi != musbet:
    b = musbet - abs(menfi)
else:
    b = 0
if menfi < musbet:
    a.append(-b)
else:
    a.append(b)
print(a)
