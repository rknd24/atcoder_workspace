n = int(input())
alist = list(map(int,input().split()))
count = 0
while True:
    flag = False
    for i in range(len(alist)):
        if alist[i] % 2 == 1:
            flag = True
            break
    if flag == True:
            break
    for j in range(len(alist)):
        alist[j] //= 2
    count +=1

print(count)

            
            
