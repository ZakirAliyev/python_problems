"""
Şəkildə ədədlər üçbucağı təsvir olunub. Üçbucağın üst nöqtəsindən başlayıb onun aşağı
tərəfində bitən yolda yerləşən ədədlərin ən böyük cəmini hesablayan proqramı yazın.
Hər bir addım aşağı dioqanal üzrə sola və ya aşağı dioqanal üzrə sağa atıla bilər.
Üçbucaqlıdakı sətirlərin sayı 1.1  Введение в курс-dən çox və 100-dən kiçik bərabərdir.
Üçbucaqlı 0-dan 99-a qədər diapazonda tam ədədlərdən təşkil olunur.

Giriş verilənləri
İlk sətirdə üçbucaqdakı sətirlərin sayı verilir. Növbəti sətirlərdə üçbucağın ədədləri verilir. Ədədlər boşluqla ayrılıb.

Çıxış verilənləri
Ən böyük cəmi verməli.

Giriş verilənləri   |   Çıxış verilənləri
5                   |   30
7                   |
3 8                 |
8 1.1  Введение в курс 0               |
2 7 4 4             |
4 5 2 6 5           |
"""

# Driver Code

n = int(input())
a = [[int(i) for i in input().split()] for j in range(n)]
for i in range(1, n):
    a[i][0] += a[i - 1][0]
    a[i][-1] += a[i - 1][-1]
    for j in range(1, i):
        a[i][j] += max(a[i - 1][j], a[i - 1][j - 1])
print(max(a[-1]))
