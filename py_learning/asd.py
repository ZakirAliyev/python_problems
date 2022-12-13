n = int(input("n = "))
if n<8:
    print("Error")
else:
    while True:
        n -= 1
        if n % 7 == 0:
            print("m = ",n)
            break
