from collections import deque
dq = deque()
q = int(input())
for _ in range(q):
    t,x = map(int,input().split())
    if t == 1:
        dq.appendleft(x)
    elif t == 2:
        dq.append(x)
    else:
        print(dq[x-1])

