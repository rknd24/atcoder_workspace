h,w = map(int,input().split())
inputlist = []
for _ in range(h):
    a = list(map(int,input().split()))
    inputlist.append(a)
#sum関数を使いたかったけど使い方がわからなかった。
hsumlist = []
wsumlist = []
#各行各列の合計計算
for i in inputlist:
    hsum = 0
    for j in i:
        hsum += j
    hsumlist.append(hsum)
for j in range(w):
    wsum = 0
    for i in range(h):
        wsum += inputlist[i][j]
    wsumlist.append(wsum)
#演算過程
bbiglist = []
for i in range(len(inputlist)):
    blist = []
    for j in range(len(inputlist[i])):
        b = 0
        b = hsumlist[i] + wsumlist[j] - inputlist[i][j]
        blist.append(b) 
    bbiglist.append(blist)
for i in range(len(bbiglist)):
    ans = " ".join(map(str,bbiglist[i]))
    print(ans)




