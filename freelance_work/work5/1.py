"""
Yazı qaydalarına görə mətndə vergüldən
sonra həmişə boşluq qoyulur. Aşağıdakı
proqram verilmiş mətndə rast gəlinən
bu növ səhvləri tapıb düzəldir. Proqramın
necə icra olunduğunu yoxlayın.
"""

s = input('Mətni daxil edin: ')
lst = list(s)
i = 0
while i < len(lst):
    if lst[i] == ',' and lst[i + 1] != ' ':
        lst.insert(i + 1, ' ')
    i = i + 1
s = ''.join(lst)
print(s)
