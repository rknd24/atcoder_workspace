s = input()
alp = "abcdefghijklmnopqrstuvwxyz"
input_list = []
flag = False
for i in s:
    input_list.append(i)
for j in alp:
    if j not in input_list:
        flag = True
        print(j)
        break
if flag == False:
    print("None")

    
  


