n,m = map(int,input().split())
count_list = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    count_list[a-1] += 1
    count_list[b-1] += 1
for i in count_list:
    print(i)



