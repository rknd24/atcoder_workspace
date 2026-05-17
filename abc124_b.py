n = int(input())
h = list(map(int,input().split()))
high_mount = 0
count = 0
for i in h:
    if i >= high_mount:
        high_mount = i
        count += 1
print(count)

