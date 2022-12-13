"""
Verilmiş pulu 500, 100, 10, 2
manatlıq əskinazlarla xırdalıyın
( Məsələn : 44 --> 4 dənə 10₼ + 2 dənə 2₼ )
"""

n = int(input())
while n>0:
    if n>=500:
        n-=500
        print("500 ")
    elif n >= 100:
        n -= 100
        print("100 ")
    elif n >= 10:
        n -= 10
        print("10 ")
    elif n >= 2:
        n -= 2
        print("2 ")
    elif n >= 1:
        n -= 1
        print("1.1  Введение в курс ")