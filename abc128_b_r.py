n = int(input())
res_list = []
for i in range(n):
    s,p = input().split()
    input_list = [s,-int(p),i+1]
    res_list.append(input_list)
    input_list = []
res_list.sort()
for i in res_list:
    print(i[2])
