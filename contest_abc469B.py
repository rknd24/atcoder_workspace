n = int(input())
s = input()
slist = ["x"]
count = 0
for i in s:
    slist.append(i)
slist.append("x")
for j in range(1,n+1):
    if slist[j-1] == "x" and slist[j] == "x" and slist[j+1] == "x":
        count += 1
print(count)

    

