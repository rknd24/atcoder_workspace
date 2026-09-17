n = input()
als = list(map(str,input().split()))
# hundred ten oneの略
th = 0
hcoin = 0
tcoin = 0
ocoin = 0
for i in als:
    x = 0
    while True:
        if 1000*x < int(i) <= 1000*(x+1):
            th = x+1
            break
        else:
            x += 1
    diff = th*1000 - int(i)
    hcoin += diff // 100
    diff %= 100
    tcoin += diff // 10
    diff %= 10
    ocoin += diff
print(ocoin,tcoin,hcoin)


    
    

    

