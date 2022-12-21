"""
Birinci simvolun özündən başqa, ilk simvolun
bütün hadisələrinin '$' olaraq dəyişdirildiyi
verilmiş sətirdən sətir əldə etmək üçün Python
proqramı yazın.
"""

def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]

    return str1


str1 = input()
print(change_char(str1))
