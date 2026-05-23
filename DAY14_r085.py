n = int(input())
kagami_ls = []
count = 0
for _ in range(n):
    d = int(input())
    kagami_ls.append(d)
kagami_ls.sort(reverse=True)
sort_ls = []
for i in kagami_ls:
    if i not in sort_ls:
        sort_ls.append(i)
        count += 1
print(count)

------------------------------------

n = int(input())
kagami_ls = []
count = 0
for _ in range(n):
    d = int(input())
    kagami_ls.append(d)
set_ls = set(kagami_ls)
print(len(set_ls))   


