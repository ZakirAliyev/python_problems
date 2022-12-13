"""
Təxmin edilən nömrə təsadüfi seçilmiş nömrədən aşağı olarsa,
istifadəçi “çox aşağı” görəcək. Təxmin edilən nömrə təsadüfi
seçilmiş nömrədən yüksəkdirsə, istifadəçi "çox yüksək" görəcək.
 İstifadəçi düzgün rəqəmi təxmin etdikdə, "sən bunu düzgün
 təxmin etdin!" çıxışda göstəriləcək.
"""

# Driver Code

import random

n = random.randrange(1, 100)
guess = int(input("Enter any number: "))
while n != guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("You guessed it right!!")
