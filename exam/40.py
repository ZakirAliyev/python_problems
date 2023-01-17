list = list(map(int, input().split()))
list1 = []
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)
