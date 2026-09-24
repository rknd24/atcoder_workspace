n,l= map(int,input().split())
k = int(input())
a = list(map(int,input().split()))

def check(x,k,l):
    last_cut = 0
    cuts = 0
    for i in a:
        if i - last_cut >= x:
            last_cut = i
            cuts += 1
    if l - last_cut < x:
        cuts -= 1
    return cuts >= k

lo,hi = 0,l
while lo < hi:
    mid = (lo + hi + 1) // 2
    if check(mid,k,l):
        lo = mid
    else:
        hi = mid - 1
print(lo)
