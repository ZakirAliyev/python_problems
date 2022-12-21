"""
Verilmiş müsbət tam ədədləri tam ədədə çevirmək üçün Python proqramı yazın.
"""

def tuple_to_int(nums):
    result = int(''.join(map(str,nums)))
    return result

nums = (1,2,3)
print("Original tuple: ") 
print(nums)
print("Convert the said tuple of positive integers into an integer:")
print(tuple_to_int(nums))

nums = (10,20,40,5,70)
print("\nOriginal tuple: ") 
print(nums)
print("Convert the said tuple of positive integers into an integer:")
print(tuple_to_int(nums))