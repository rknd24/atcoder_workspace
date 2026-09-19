n = int(input())
s = input()
t = input()
flag = True
for i in range(n):
    if t[i] == "*" or s[i] == t[i]:
        flag = True
    else:
        flag = False
        break
if flag == True:
    print("Yes")
elif flag == False:
    print("No")



