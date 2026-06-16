n,m,c = map(int,input().split())
b = list(map(int,input().split()))
count = 0
for _ in range(n):
    a = list(map(int,input().split()))
    ans = c
    for i in range(m):
        ans += a[i]*b[i]
    if ans > 0:
        count += 1
print(count)

