n,s,l = map(int,input().split())
alst = list(map(int,input().split()))
# nが街の数　sが初期地点　lが移動できる距離の最大値
# 1方向に探索してLを超してしまった、だから次は別のルートを探そうでは計算量がきつい？
# やっぱり二分探索か
# 累積和？
flst = alst[:s-1]
slst = alst[s-1:]
ans = 0
if len(flst) <= len(slst):
    if sum(slst) <= l:
        print(len(slst)+1)
    else:
        while ans <= l:
            for i in range(len(flst)):
                if flst[-i+1]*2 < slst[-(i+1)] and sum(slst[:-(i+1)])+flst[-(i+1)]*2 <= l:
                    ans = (i+1)*2 + sum(slst[:-(i+1)])
else:
    if sum(flst) <= l:
        print(len(slst)+1)




    

    