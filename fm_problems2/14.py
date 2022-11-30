"""
14. Verilmiş M ədədinin daxil edilmiş (a, b)
intervalına daxil olub olmadığını yoxlayın.
(Nümunə : m= 5 , (3, 8) Yes ; m = -1 , (0,9) No )
"""

n = int(input)
a = int(input)
b = int(input)
if n > a and n < b:
    print("This number is included to the interval")
else:
    print("This number isn't included to the interval")
