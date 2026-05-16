n,m = map(int,input().split())
count_list = [0]*m
count = 0
for i in range(n):
    like_list = list(map(int,input().split()))
    for f in like_list[1:]:
        count_list[f-1] += 1
for j in count_list:
    if j == n:
        count += 1
print(count)


