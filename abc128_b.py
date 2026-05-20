n = int(input())
res_list = []
for i in range(n):
    s,p = input().split()
    res_list.append([s,-int(p),i+1])
res_list.sort()
for j in res_list:
    print(j[2])


