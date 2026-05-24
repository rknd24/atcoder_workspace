n = int(input())
a = list(map(int,input().split()))
count = 0
while True:
    for i in a:
        if i % 2 == 1:
            print(count)
            exit()
        else:
            continue
    for j in range(n):
        a[j] //= 2
    count += 1



    
    

            
