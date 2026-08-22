import bisect
n = int(input())
a = list(map(int,input().split()))
q = int(input())
a.sort()
for _ in range(q):
    b = int(input())
    idx = bisect.bisect_left(a,b)
    if idx != 0 and idx != len(a):
        s_diff = abs(a[idx-1]-b)
        b_diff = abs(a[idx]-b)
        if s_diff <= b_diff:
            print(s_diff)
        else:
            print(b_diff)
    if idx == 0:
        print(a[idx]-b)
    if idx == len(a):
        print(abs(a[len(a)-1]-b))
