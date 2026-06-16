a,b = map(int,input().split())
s = input()
flag = False
count = 0
s_list = []
search = ["0","1","2","3","4","5","6","7","8","9","-"]
for i in s:
    s_list.append(i)
if len(s_list) != a+b+1:
    flag = True
for j in range(len(s)):
    if s_list[j] == "-":
        count += 1
    if s_list[j] not in search:
        flag = True
if count != 1:
    flag = True
if s[a] != "-":
    flag = True
if flag == False:
    print("Yes")
else:
    print("No")


    
