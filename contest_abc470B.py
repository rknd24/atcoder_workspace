n = int(input())
c = list(map(int,input().split()))
s = set()
count = 0
countlist = [0] * (n+1)
for i in c:
    countlist[i] += 1
countlist.sort()
print(n-countlist[-1])



        

    


