a = input()
if a[0] == "-":
    if a[1] == a[2]:
        print(a)
    elif a[2] == "0":
        print(a[0:2])
elif a[1] == "0":
    print(a[0:1])
elif a[0] == a[1]:
    print(a)
