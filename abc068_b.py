n = int(input())
count_list = []
max_count = -1
ans = 1
for i in range(1,n+1):
    temp_i = i
    count = 0
    while temp_i % 2 == 0:
        temp_i /= 2
        count += 1
    if count > max_count:
        max_count = count
        ans = i
print(ans)
   



        
        

