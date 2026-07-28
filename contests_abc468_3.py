n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
count = 0
for i in range(n):
    if p[i] > q[i]:
        print(count)
        break
    else:
        if p[i+1] > q[i+1]:
         print(count)
         break
    
        


        