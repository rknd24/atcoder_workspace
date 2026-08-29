n,k = map(int,input().split())
a = list(map(int,input().split()))
count = 0
countlist = [0]*(2*10**5)
obj = {}
for x in range(k+1):
    obj[x] = 0
for i in range(n):
    if obj[a[i]] == 0:
        obj[a[i]] = 1
        countlist[a[i]-1] += 1
    else:
        obj[a[i]] += 1
        countlist[a[i]-1] += 1
countlist.sort()
for j in range(1,k+1):
    if obj[j]+1 >= countlist[-1]:
        count += 1
print(count)





    
     
