"""
Aşağıdakı nümunədə siyahı
10 təsadüfi ədəddən düzəldilir
və onlar siyahiya yigilir
"""

from random import randint
m = [randint(10, 20) for i in range(10)]
print(m)
