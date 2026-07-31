h,w = map(int,input().split())
cell_h = 0
cell_w = 0
if h != 1 and w != 1:
    cell_h = ((h+1)//2)
    cell_w = ((w+1)//2)
    ans = cell_h*cell_w
else:
    if h == 1:
        ans = w
    elif w == 1:
        ans = h
print(ans)