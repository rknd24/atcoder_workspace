# 2<=N<=10^5
# N-1 <= M <= 10^5
#自分自身より頂点番号が小さい隣接頂点がちょうど1つある
n,m = map(int,input().split())
ans = 0
count = [0]*(10**5+1)
for _ in range(m):
    a,b = map(int,input().split())
    if a > b:
        count[a]+=1
    else:
        count[b]+=1

for j in count:
    if j == 1:
        ans+=1
print(ans)


