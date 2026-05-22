n = int(input())
input_list = []
flag = False
for i in range(n):
    w = input()
    if i == 0:
        prev_word = w[-1]
        continue
    else:
        if prev_word != w[0]:
            flag = True
            break
        else:
            if w not in input_list:
                input_list.append(w)
                prev_word = w[-1]
                continue
            else:
                flag = True
                break

if flag == False:
    print("Yes")
else:
    print("No")


