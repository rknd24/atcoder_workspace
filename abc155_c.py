from collections import Counter
n = int(input())
input_list = []
dic = {}
for s in range(n):
    s = input()
    input_list.append(s)
dic = Counter(input_list)

max_count = 0
for i in dic:
    if dic[i] >= max_count:
        max_count = dic[i]

ans_list = []
for i in dic:
    if dic[i] == max_count:
        ans_list.append(i)
ans_list.sort()
for i in ans_list:
    print(i)
    

        





