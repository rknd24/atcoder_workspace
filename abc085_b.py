n = int(input())
mochi_list = []
for i in range(n):
    mochi = int(input())
    mochi_list.append(mochi)
lst_list = []

#一旦ソートして降順にする。その後重複を防ぐため
mochi_list.sort(reverse=True)
for mochi in mochi_list:
    if mochi not in lst_list:
        lst_list.append(mochi)

print(len(lst_list))

