"""
Verilmiş sətirin rəqəmlərinin cəmini
hesablamaq üçün Python proqramı yazın.
"""


def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit


a = input()
print(sum_digits_string(a))
