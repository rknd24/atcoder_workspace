n = int(input())
alist = list(map(int,input().split()))
now = 0 #現在位置
count = 0 #合計移動距離
diflist = [] #差分のリスト
for i in alist:
    dif = i-now
    diflist.append(dif)
diflist.sort(key=abs) #Webで調べた
count += abs(diflist[0])
now = diflist[0] #今回も累積和の類いかな