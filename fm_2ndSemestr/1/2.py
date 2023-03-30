def polindrom(n):
    sum = 0
    for digit in set(n):
        count = n.count(digit)
        if count % 2:
            sum += 1
    if sum > 1:
        print("This number is pseudo palindrome")
    else:
        print("This number is not pseudo palindrome")


n = input()
b = n[::-1]
if b == n:
    print("This number is not pseudo palindrome")
else:
    polindrom(n)