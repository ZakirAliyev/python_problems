num = input()
n = len(num)
seen = set()
best_seq = ''
i = j = 0

while j < n:
    if num[j] not in seen:
        seen.add(num[j])
        j += 1
        if j - i > len(best_seq):
            best_seq = num[i:j]
    else:
        seen.remove(num[i])
        i += 1

print(best_seq)
