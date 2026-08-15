n = int(input())
slist = []
count = [1]*100
for _ in range(n):
    s = input().upper()
    if s not in slist:
        slist.append(s)
    else:
        for i in range(len(slist)):
            new_s = slist[i]
            if new_s.upper() == s.upper():
                count[i] += 1
count.sort(reverse=True)
print(count[0])


        
    