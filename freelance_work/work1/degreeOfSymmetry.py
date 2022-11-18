"""
Natural ədədin onluq yazılışında rəqəmləri eyni olan
və bu ədədin onluq yazılışının mərkəzinə nəzərən
simmetrik yerləşən cütlüklərin sayını həmin ədədin
simmetriya dərəcəsi adlandıracağıq. Əgər ədəddə hər
hansı rəqəm onluq yazılışda ortada yerləşirsə,
onu da özü ilə bir cütlük kimi saymaq lazımdır.
n ədədinin simmetriya dərəcəsini tapın.

Giriş verilənləri
Giriş sətrində yeganə bir n (n < 2 ·109) natural ədədi verilir.

Çıxış verilənləri
Çıxışa yeganə bir ədəd - n ədədinin simmetriya dərəcəsini verməli.

Giriş verilənləri   |   Çıxış verilənləri
123322              |   2
"""

# Driver Code

x = 0
n = input()
a = len(n)
if (int(a) % 2 == 1):
    x += 1
for i in range(0, int(a) // 2):
    if (n[i] == n[a - (i + 1)]):
        x += 1
print(x)