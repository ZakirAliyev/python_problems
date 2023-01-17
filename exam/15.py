list = list(map(int, input().split()))
min = list[0]
for i in list:
    if i < min:
        min = i
print("max = ", min)
