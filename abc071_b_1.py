s = input()
first_list=[]
for i in s:
    first_list.append(i)
first_list.sort()
count_list = [0]*26
for j in first_list:
    number = ord(j)-ord("a")
    count_list[number] += 1
if 0 in count_list:
    final_num = count_list.index(0)
    final_str = chr(final_num+ord("a"))
else:
    print("None")


print(final_str)




