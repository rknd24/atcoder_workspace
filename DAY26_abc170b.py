x,y = map(int,input().split())
turu = 2
kame = 4
flag = False
for i in range(x+1):
    for j in range(x+1):
        if i*turu + j*kame == y and i + j == x:
            flag = True
if flag == False:
    print("No")
if flag == True:
    print("Yes")

    
