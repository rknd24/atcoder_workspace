n = int(input())
input_list = []
dic = {}
for s in range(n):
    s = input()
    input_list.append(s)
for i in input_list:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
max_count = 0
ans = []
for i in dic:
    if dic[i] > max_count:
        max_count = dic[i]
        ans = []
        ans.append(i)
    elif dic[i] == max_count:
        ans.append(i)

ans.sort()
for i in ans:
    print(i)

