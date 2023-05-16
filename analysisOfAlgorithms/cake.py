def calculate_max_slices(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        slices = 1
        for i in range(1, n + 1):
            slices += i
        return slices


n = int(input("Count of cut: "))
max_slices = calculate_max_slices(n)
print("Maximum count of slices:", max_slices)