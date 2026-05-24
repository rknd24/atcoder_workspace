s = input()
flag = False
s_list = []
alp = "abcdefghijklmnopqrstuvwxyz"
for i in s:
    s_list.append(i)
s_list.sort()
for i in alp:
    if i not in s_list:
        flag = True
        print(i)
        break
    else:
        continue
if flag == False:
    print("None")

