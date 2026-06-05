n,m = map(int,input().split())
stores = []
for _ in range(n):
    a,b = map(int,input().split())
    stores.append([a,b])
    
stores.sort()
ans = 0 #合計金額
bought = 0 #何本購入したか
for a,b in stores:
    if bought+b <= m:
        ans += a*b
        bought += b
    else:
        x = m - bought
        ans += a*x
        bought += x
        break
print(ans)
        



