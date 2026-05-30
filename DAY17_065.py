n = int(input())
inp = []
for _ in range(n):
    a = int(input())
    inp.append(a)
count = 1
now = 1
loop = 0
while inp[now-1] != 2 and loop != n:
    now = inp[now-1]
    count+=1
    loop+=1

if loop != n:
    print(count)
else:
    print(-1)
    



