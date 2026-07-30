n = int(input())
s_set = set()
datelist = []
for i in range(n):
    s = input()
    if s not in s_set:
        s_set.add(s)
        datelist.append(i+1)
    else:
        continue
for j in range(len(datelist)):
    print(datelist[j])

