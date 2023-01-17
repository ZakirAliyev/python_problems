list = list(map(int, input().split()))
max = list[0]
for i in list:
    if i > max:
        max = i
print("max = ", max)
