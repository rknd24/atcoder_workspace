n = int(input())
cum1 = [0]*(n+1)
cum2 = [0]*(n+1)
for i in range(n):
    """ここで二次元配列を作って後から各クエリの合計点数を一つずつ計算
    するのは計算量的に不可。O(N*Q)となる。このQは計算量の上限。計算量は
    ここまで計算しうる可能性があるで算出。今回は計算量を減らすために累積和
    を使うことでO(N+Q)に落とせる"""
    c,p = map(int,input().split())
    if c == 1:
        cum1[i+1] = cum1[i] + p
        cum2[i+1] = cum2[i] + 0
    elif c == 2:
        cum1[i+1] = cum1[i] + 0
        cum2[i+1] = cum2[i] + p
q = int(input())
for j in range(q):
    l,r = map(int,input().split())
    sum1 = cum1[r] - cum1[l-1]
    sum2 = cum2[r] - cum2[l-1]
    print(sum1,sum2)

    
        


