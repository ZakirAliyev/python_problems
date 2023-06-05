def ikil(n):
    bi = bin(n)[2:]
    count = bi.count('1')
    return count


n = int(input())

birl = ikil(n)

print(birl)
