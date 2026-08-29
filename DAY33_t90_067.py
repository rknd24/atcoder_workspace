from collections import deque
n,k = map(int,input().split())
str_n = str(n)
new_n = int(str_n,8)
for _ in range(k):
    remque = deque()
    while new_n >= 9:
        rem = new_n % 9
        remque.appendleft(rem)
        new_n //= 9
    if new_n == 8:
        new_n = 5
    for i in range(len(remque)):
        if remque[i] == 8:
            remque[i] = 5
    ans = str(new_n)
    for j in remque:
        ans += str(j)
        new_n = int(ans,8)
print(ans)
    


            
        
