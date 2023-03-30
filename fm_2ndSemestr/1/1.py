f = open("data1.txt", "r")
a = f.read()

b = a[::-1]

if a == b:
    print("This number is a Palindrome")
else:
    print("This number is not a Palindrome")