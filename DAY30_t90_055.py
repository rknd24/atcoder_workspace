n, p, q = map(int, input().split())
a = list(map(int, input().split()))
rl = [x % p for x in a]
count = 0
for i in range(n):
    ri = rl[i]
    for j in range(i+1, n):
        rij = ri * rl[j] % p
        for k in range(j+1, n):
            rijk = rij * rl[k] % p
            for l in range(k+1, n):
                rijkl = rijk * rl[l] % p
                for o in range(l+1, n):
                    if rijkl * rl[o] % p == q:
                        count += 1
print(count)

