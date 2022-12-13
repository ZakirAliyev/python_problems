"""
Ədədin simmetriya dərəcəsini hesablayın.

Giriş Verilənləri:   |   Çıxış verilənləri :
123321               |   3
123322               |   2
"""

sum = 0
a = input("a = ")
b = a[::-1]
for i in range(0,len(a)):
    if a[i]==b[i]:
        sum+=1
print("Simmetriya derecesi :",end=" ")
if len(a)%2==0:
    print(sum // 2)
else:
    print(sum // 2 + 1)