n,m = map(int,input().split())
count_list = [0]*m
count = 0
for i in range(n):
    k = list(map(int,input().split()))
    for j in k[1:]:
        count_list[j-1] += 1
for i in count_list:
    if i == n:
        count += 1
print(count)

"""-----------------------------------------"""
n,m = map(int,input().split())
common_foods = set(range(1,m+1))

for _ in range(n):
    data = list(map(int, input().split()))
    liked_list = set(data[1:])
    common_foods &= liked_list
print(common_foods)





