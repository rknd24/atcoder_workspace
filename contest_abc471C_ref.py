n = int(input())
neg = []
pos = []
a = list(map(int,input().split()))
for i in a:
    if i == abs(i):
        pos.append(i)
    else:
        neg.append(i)
pos.sort(key=abs)
neg.sort(key=abs)
i,j = 0,0
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
        total += abs(neg[i]-cur)
        cur = neg[i]
        i += 1
    else:
        total += abs(pos[j]-cur)
        cur = pos[j]
        j += 1
print(total)
            

