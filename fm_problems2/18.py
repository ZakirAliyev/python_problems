"""
18. Tərəfləri a, b və c, d olan 2 düzbucaqlı verilmişdir.
Onların birinin digərinin içinə yerləşdiyini yoxlayın.
Yerləşmə elə olmalıdır ki, içəridəki düzbucaqlının hər
bir tərəfi çöldəki duzbucaqlının tərəfinə ya paralel
ya da perpendikulyar olsun.
"""

a,b,c,d = map(int,input("a, b, c, d = ").split())

if (a<c and b<d) or (a<d and b<c) or (a>c and b>d) or (a>d and b>c):
    print("Nested in each other.")
else:
    print("They are not nested.")
