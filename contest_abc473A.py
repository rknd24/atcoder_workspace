n = int(input())
a = list(map(int,input().split()))
half = []
for i in range(n//2):
    half.append(a[i])
print(sum(a)-sum(half))
    