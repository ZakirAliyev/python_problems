"""
Lüğətdə maksimum dəyərin açarını tapmaq üçün Python proqramı yazın.

Verilmiş lüğətdə maksimum dəyərin açarını tapmaq və qaytarmaq üçün açar parametri dict.get() olaraq təyin edilmiş max()-dan istifadə edin.
Verilmiş lüğətdə minimum dəyərin açarını tapmaq və qaytarmaq üçün əsas parametri dict.get() olaraq təyin edilmiş min() funksiyasından istifadə edin.
"""

def test(d):
  return max(d, key = d.get), min(d, key = d.get)

students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
print("\nOriginal dictionary elements:")
print(students)
print("\nFinds the key of the maximum and minimum value of the said dictionary:")
print(test(students))