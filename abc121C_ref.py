n,m = map(int,input().split())
dimarray = []
ans = 0
bought = 0
i = 0
for _ in range(n):
    a,b = map(int,input().split())
    dimarray.append([a,b])
dimarray.sort(key=lambda x: x[0])
while bought < m:
    if m - bought >= dimarray[i][1]:
        ans += dimarray[i][0] * dimarray[i][1]
        bought += dimarray[i][1]
        i += 1
    else:
        ans += dimarray[i][0] * (m-bought)
        bought += m - bought
print(ans)



    

    
    

    
