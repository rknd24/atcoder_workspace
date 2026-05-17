n = int(input())
max_size = -1
ans = 1
for i in range(1,n+1):
    count = 0
    temp_i = i
    while temp_i % 2 == 0:
        temp_i /= 2
        count += 1
    if count > max_size:
        max_size = count
        ans = i
print(ans)

    
    