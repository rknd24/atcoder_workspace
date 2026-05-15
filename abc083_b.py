n,a,b = map(int,input().split())
count = []

#nを文字列変換か10で割ったあまりで考える

for i in range(n+1):
    temp_i = str(i)
    total = 0
    for j in temp_i:
        total += int(j)

    if a <= total <= b:
        count.append(i)

sum = 0
for i in count:
    sum += i

print(sum)

    

    
