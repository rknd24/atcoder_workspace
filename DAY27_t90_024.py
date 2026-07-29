n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ab = 0
for i in range(n):
    ab += abs(a[i]-b[i])
dif = k - ab
if dif % 2 == 0 and dif >= 0:
    print("Yes")
else:
    print("No")
