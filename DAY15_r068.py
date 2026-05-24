n = int(input())
max_count = -1
for i in range(1,n+1):
    count = 0
    temp_i = i
    while temp_i % 2 == 0:
        count += 1
        temp_i /= 2
        if count > max_count:
                max_count = count
                ans = i
print(ans)


   
