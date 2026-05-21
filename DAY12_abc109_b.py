n = int(input())
input_list = []
flag = False
for i in range(n):
    s = input()
    if input_list == []:
        input_list.append(s)
        continue
    else:
        if s[0] == input_list[i-1][-1]:
            if s not in input_list:
                input_list.append(s)
                continue
            else:
                flag = True
                break
        else:
            flag = True
    
if flag == False:
    print("Yes")
else:
    print("No")


        

