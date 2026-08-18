n = int(input())
a = list(map(int,input().split()))
neg = []
pos = []
i = 0
j = 0
for k in a:
    if k != abs(k):
        neg.append(k)
    else:
        pos.append(k)
neg.sort(reverse=True)
pos.sort()
cur = 0
total = 0
while i < len(neg) or j < len(pos):
    if i < len(neg) and j < len(pos):
        d_neg = abs(neg[i]-cur)
        d_pos = abs(pos[j]-cur)
        if d_neg <= d_pos:
            total += d_neg
            cur = neg[i]
            i += 1
        else:
            total += d_pos
            cur = pos[j]
            j += 1
    elif i < len(neg):
        d_neg = abs(neg[i]-cur)
        total += d_neg
        cur = neg[i]
        i += 1
    else:
        d_pos = abs(pos[j]-cur)
        total += d_pos
        cur = pos[j]
        j += 1
print(total)