"""
Sətirdə əlifbanın bütün hərflərinin olub
olmadığını yoxlamaq üçün Python proqramı yazın.
"""

import string
alphabet = set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)