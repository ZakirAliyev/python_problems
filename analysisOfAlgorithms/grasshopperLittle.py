def function(n):
    f = 1
    f1 = 2
    f2 = 3

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3, n):
            f = f1
            f1 = f2
            f2 = f + f1

        return f2


n = int(input())
print(function(n))
