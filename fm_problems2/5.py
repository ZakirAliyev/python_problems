"""
5. Ölçüləri A,B,C olan bir qutu verilib.
Ölçüləri M və N olan qapıdan bu qutu keçərmi?
"""

m, n, a, b, c = map(int, input().split())
if (m > a and n > b) or (n > a and m > b) or (m > a and n > c) or (n > a and m > c) or (m > c and n > b) or (
        n > c and m > b):
    print("Yes, it will pass.")
else:
    print("No, it won't pass.")
