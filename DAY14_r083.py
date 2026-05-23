n,a,b = map(int,input().split())
count = 0
for i in range(1,n+1):
   temp_i = i
   d_sum = 0
   while temp_i != 0:
    d_sum += temp_i % 10
    temp_i //= 10
   if a <= d_sum <= b:
     count += i
print(count)
     

    
