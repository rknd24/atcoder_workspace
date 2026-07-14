n,m = map(int,input().split())
ablist = []
for _ in range(n):
  a,b = map(int,input().split())
  ablist.append([a,b])
ablist.sort(key=lambda ls:ls[0])
ans = 0
bought = 0
for a,b in ablist:
  if bought+b <= m:
    ans += a*b
    bought += b
  else:
    ans += a*(m-bought)
    bought += m-bought
print(ans)