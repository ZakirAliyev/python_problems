"""
23. Programa il daxil edilir. Daxil edilmiş ilə
əsasən bu ilin uzun il olub olmadığını yoxlayın.
"""

def Leap(year):
    if ((year % 400 == 0) or
            (year % 100 != 0) and
            (year % 4 == 0)):
        print("This year is long year.");
    else:
        print("This year isn't long year")


year = int(input("Please, enter the year: "))

Leap(year)
