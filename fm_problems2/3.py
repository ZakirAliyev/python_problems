"""
3. Natural ədəd verilmişdir. Bu ədədin tək
və 7-ə bölünən ədəd olduğunu müəyyən edin.
"""

n = int(input())
if (n % 2 == 1 and n % 7 == 0):
    print("This number is odd and divided by 7")
else:
    print("This number is not odd and divided by 7")