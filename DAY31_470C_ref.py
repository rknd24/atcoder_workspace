n,q = map(int,input().split())
a = [0]*(n)
ans = 0
idxs = []
for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        old = a[query[1]-1]
        if old == 0:
            idxs.append(query[1]-1)
        new = old+1
        ans = ans^old^new
        a[query[1]-1] += 1
        print(ans)
    else:
        new_idxs = []
        for x in idxs:
            ans ^= a[x]
            a[x] -= 1
            ans ^= a[x]
            if a[x] != 0:
                new_idxs.append(x)
            idxs = new_idxs
        print(ans)
