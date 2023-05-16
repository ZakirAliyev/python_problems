def function(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    elif n == 3:
        return 7
    else:
        return function(n - 1) + function(n - 2) + function(n - 3)


n = int(input())
print(function(n))
