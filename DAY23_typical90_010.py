n = int(input())
cum1 = [0]*(n+1)
cum2 = [0]*(n+1)
for i in range(n):
    c,p = map(int,input().split())
    if c == 1:
         cum1[i+1] = cum1[i] + p
         cum2[i+1] = cum2[i] + 0
    elif c == 2:
         cum2[i+1] = cum2[i] + p
         cum1[i+1] = cum1[i] + 0
q = int(input())
for _ in range(q):
     l,r = map(int,input().split())
     print(cum1[r]-cum1[l-1],cum2[r]-cum2[l-1])
    
     
    
    


    
        