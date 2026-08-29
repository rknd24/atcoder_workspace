n = int(input())
a = list(map(int,input().split()))
countlist = [0]*101
diff = 0
for i in range(n):
    countlist[a[i]] += 1
    if countlist[a[i]] == 2:
        diff += a[i]*2
        countlist[a[i]] = 0
print(sum(a) - diff)
        
    



