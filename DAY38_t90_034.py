n,k = map(int,input().split())
a = list(map(int,input().split()))
# iが前方、jが後方のポインタ
i,j = 0,0
ans = 0
cnt = {}
for _ in range(n):
    cnt[a[i]] = cnt.get(a[i],0) + 1
    i += 1
    if len(cnt) > k:
        if cnt[a[j]] != 1:
            cnt[a[j]] -= 1
        else:
            del cnt[a[j]]
        j += 1
    ans = max(ans,i-j)
print(ans)

    
